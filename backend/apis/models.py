from django.db import models
from utils.models import GUIDModel
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.
import reversion

#version mixin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import json
from django.utils.functional import cached_property
from django.core.serializers.json import DjangoJSONEncoder
import uuid
from django.utils.timezone import now

User = get_user_model()
class Course(GUIDModel): #AKA classroom
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=6, blank=True, null=True)
    
    
    @classmethod
    def get_domain_from_request_host(cls, request_host):
        return [s for s in request_host.split('.') if s != 'www'][0] if request_host else None
    

@reversion.register()
#register to use reversion with api. run python manage.py createinitialrevisions
class Assignment(GUIDModel):
    title = models.CharField(max_length=256)
    subject = models.ForeignKey('Subject', related_name='assignments', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.subject} Assignment: {self.title}"
    

class Subject(GUIDModel):
    title = models.CharField(max_length=256)
    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    
    def __str__(self) -> str:
        return f"{self.title} {self.code}"

class Discussion(GUIDModel):
    pass

class Post(GUIDModel):
    content = models.TextField(max_length=1000)
    poster = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="posts")
    likes = models.IntegerField(default=0)
    likers = models.ManyToManyField('Profile', blank=True, related_name="posts_liked")

    def __str__(self):
        return f" \n Post: {self.content} by {self.poster} \n  {self.likers.all().count()} likes"

    def num_likes(self):
        return self.likers.all().count()

    pass

class PostComment(GUIDModel):
    pass

class Comment(GUIDModel):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_made")
    content = models.CharField(max_length=200)
    #date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.poster)


class Profile(GUIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')


class VersionedModelMixin(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=255)
    content_object = GenericForeignKey('content_type', 'object_id')
    version_number = models.PositiveIntegerField()
    comments = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    fields_json = models.JSONField(encoder=DjangoJSONEncoder)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        abstract = True

    def __str__(self):
        return f"Version {self.version_number} of {self.content_object}"

    def revert(self):
        #revert the original model to this version
        fields_json = self.fields_json
        for field_name, field_value in fields_json.items():
            setattr(self.content_object, field_name, str(field_value))
        self.content_object.save()

    def register_model(self):
        #save some extra information here
        pass

    @classmethod
    def create_version(cls, instance, creator, version_number=None):

        #TODO make creator request.user
        fields_json = {}
        for field in instance._meta.fields:
            if isinstance(field, models.ForeignKey):
                #for ForeignKey fields, store the primary key
                print("FIELD ATTNAME", field.attname)
                fields_json[field.name] = str(getattr(instance, field.attname))
            elif isinstance(field, models.ManyToManyField):
                #for ManyToMany fields, store the primary keys of related instances
                fields_json[field.name] = [related_instance.pk for related_instance in getattr(instance, field.name).all()]
            else:
                fields_json[field.name] = str(getattr(instance, field.name))
        
        if not version_number:
            #if version_number is not provided, calculate the highest version_number + 1
            highest_version = cls.objects.filter(content_type=ContentType.objects.get_for_model(instance), object_id=str(instance.pk)).order_by('-version_number').first()
            version_number = highest_version.version_number + 1 if highest_version else 1


        version = cls(
            content_type=ContentType.objects.get_for_model(instance),
            object_id=str(instance.pk),
            content_object=instance,
            version_number=version_number,
            fields_json=fields_json,
            creator=creator
        )
        version.save()
    
    def deserialize_json_fields(self):
        fields_json = self.fields_json
        for field_name, field_value in fields_json.items():
            field = self._model._meta.get_field(field_name)
            if isinstance(field, models.ManyToManyField):
                related_model = field.related_model
                related_instances = related_model.objects.filter(pk__in=field_value)
                fields_json[field_name] = related_instances
            elif isinstance(field, models.ForeignKey):
                related_model = field.related_model
                try:
                    related_instance = related_model.objects.get(pk=field_value)
                    fields_json[field_name] = related_instance
                except related_model.DoesNotExist:
                    pass  # Raise some exception
            elif isinstance(field, models.UUIDField):
                fields_json[field_name] = uuid.UUID(field_value)
            else:
                fields_json[field_name] = field_value
        return fields_json
    
    # @cached_property
    # def instantiate(self):
    #     #create an instance of the associated model using the fields stored in the version
    #     model_class = self.content_type.model_class()
    #     instance = model_class()

    #     for field_name, field_value in self.fields_json.items():
    #         field = model_class._meta.get_field(field_name)
    #         if isinstance(field, models.ManyToManyField):
    #             #for manytomany fields, handle them separately
    #             self.instantiate_many_to_many(instance, field_name, field_value)
    #         elif isinstance(field, models.ForeignKey):
    #             #for foreign key, retrieve the related model instance
    #             related_model = field.related_model
    #             try:
    #                 related_instance = related_model.objects.get(pk=field_value)
    #                 setattr(instance, field_name, related_instance)
    #             except related_model.DoesNotExist:
    #                 pass  #raise some exception
    #         elif isinstance(field, models.UUIDField):
    #             #for uuid fields, convert string back to uuid
    #             setattr(instance, field_name, uuid.UUID(field_value))
    #         else:
    #             setattr(instance, field_name, field_value)

    #     return instance
    
    # def instantiate_many_to_many(self, instance, field_name, field_value):
    #     #handle manytomany
    #     field = instance._meta.get_field(field_name)
    #     related_model = field.related_model
    #     related_instances = related_model.objects.filter(pk__in=field_value)
    #     setattr(instance, field_name, related_instances)
    
    @cached_property
    def instantiate(self):
        model_class = self.content_type.model_class()
        instance = model_class(**self.deserialize_json_fields())
        return instance


    @property
    def _model(self):
        return self._content_type.model_class()
    
    @property
    def _content_type(self):
        return ContentType.objects.db_manager(self._state.db).get_for_id(self.content_type_id)
    

class PostVersion(VersionedModelMixin):
    pass