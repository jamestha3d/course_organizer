from django.db import models
from utils.models import GUIDModel
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core import serializers
# Create your models here.
import reversion


#imports for version model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.timezone import now
import json
from django.utils.functional import cached_property
import uuid
User = get_user_model()

class Course(GUIDModel): #AKA classroom
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=6, blank=True, null=True)
    #students = models.ManyToManyField()
    
    
    @classmethod
    def get_domain_from_request_host(cls, request_host):
        return [s for s in request_host.split('.') if s != 'www'][0] if request_host else None
    

@reversion.register()
#register to use reversion with api. run python manage.py createinitialrevisions
class Assignment(GUIDModel):
    title = models.CharField(max_length=256)
    subject = models.ForeignKey('Subject', related_name='assignments', on_delete=models.CASCADE)
    #due = models.DateTimeField()
    
    def __str__(self) -> str:
        return f"{self.subject} Assignment: {self.title}"
    

class Subject(GUIDModel):
    title = models.CharField(max_length=256)
    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    
    def __str__(self) -> str:
        return f"{self.title} {self.code}"

class Submission(GUIDModel):
    pass
class Discussion(GUIDModel):
    pass

class Post(GUIDModel):
    content = models.TextField(max_length=1000)
    poster = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="posts")
    likes = models.IntegerField(default=0)
    likers = models.ManyToManyField('Profile', blank=True, related_name="posts_liked")

    def __str__(self):
        return f" \n Post: {self.content}"  # by {self.poster}"\n  {self.likers.all().count()} likes"

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

    # def __str__(self):
    #     return (f'{self.user.email}' if self.user else 'None')

class Student(GUIDModel):
    pass

class Teacher(GUIDModel):
    pass


from django.core.serializers.json import DjangoJSONEncoder
class VersionedModelMixin(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=255)
    content_object = GenericForeignKey('content_type', 'object_id')
    version_number = models.PositiveIntegerField()
    comments = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    fields_snapshot = models.JSONField(encoder=DjangoJSONEncoder)
    created = models.DateTimeField(default=now)
    # format = models.CharField(
    #     max_length=255,
    #     help_text="The serialization format used by this model.",
    # )

    class Meta:
        ordering = ['-created']
        abstract = True

    def __str__(self):
        return f"Version {self.version_number} of {self.content_object}"

    def revert(self):
        # Revert the original model to this version
        fields_snapshot = self.fields_snapshot
        for field_name, field_value in fields_snapshot.items():
            setattr(self.content_object, field_name, str(field_value))
        self.content_object.save()

    def register_model(self):
        #we need to know for foreign keys which attr to save
        pass
    @classmethod
    def create_version(cls, instance, creator, version_number=None):
        # Store the fields as a JSON snapshot
        #fields_snapshot = {field.name: str(getattr(instance, field.name)) for field in instance._meta.fields}
        fields_snapshot = {}
        for field in instance._meta.fields:
            if isinstance(field, models.ForeignKey):
                # For ForeignKey fields, store the primary key
                print("FIELD ATTNAME", field.attname)
                fields_snapshot[field.name] = str(getattr(instance, field.attname))
            else:
                fields_snapshot[field.name] = str(getattr(instance, field.name))
        
        if not version_number:
            # If version_number is not provided, calculate the highest version_number + 1
            highest_version = cls.objects.filter(content_type=ContentType.objects.get_for_model(instance), object_id=str(instance.pk)).order_by('-version_number').first()
            version_number = highest_version.version_number + 1 if highest_version else 1


        version = cls(
            content_type=ContentType.objects.get_for_model(instance),
            object_id=str(instance.pk),
            content_object=instance,
            version_number=version_number,
            fields_snapshot=fields_snapshot,
            creator=creator
        )
        version.save()

    #@cached_property
    # def instantiate(self):
    #     model_class = self.content_type.model_class()
    #     print("MODEL CLASS", model_class)
    #     #check the type of each field:
    #     data= self.deserialize_fields_snapshot()
    #     class_fields = self._meta.get_fields()
    #     return list(serializers.deserialize(self.format, data, ignorenonexistent=True,
    #                     use_natural_foreign_keys=version_options.use_natural_foreign_keys))[0]
        #print("FIELDS", fields, "CLASS", class_fields)
        # for field in class_fields:
        #     if field.name in fields:

        #     print(field.name)
        # #instance = model_class(**fields)
        #instance = model_class(**json.loads(self.fields_snapshot))
        #return instance
    
    def deserialize_fields_snapshot(self):
        # Deserialize the JSON snapshot, handling non-serializable fields
        print('deserializing....')
        fields_snapshot = self.fields_snapshot
        print("FIELDS SNAPSHOT", fields_snapshot)
        for field_name, field_value in fields_snapshot.items():
            print("CHECKING FIELD ", field_name, field_value)
            if not isinstance(field_value, str) and not isinstance(field_value, int) and not isinstance(field_value, float):
                # If the field is not JSON serializable, handle it appropriately
                print('FOUND NON DESERIALIXZABLE FIELD')
                print(field_name, field_value)
                field_value = self.deserialize_non_serializable_field(field_name, field_value)
            fields_snapshot[field_name] = field_value
            if isinstance(field_value, models.Model):
                print("MODEL FOUND", field_name)
        print("DONE")
        return fields_snapshot

    def deserialize_non_serializable_field(self, field_name, field_value):
        print('deserializing non serializable fields')
        # Implement custom logic to handle non-serializable fields
        # For example, you can convert datetime objects to strings or handle other types
        # Here, we'll just use str() as an example
        if isinstance(field_value, models.Model):
            # For ForeignKey fields, store the primary key
            #return field_value.pk
            print(field_value)
            return field_value
        return str(field_value)
    
    #@cached_property
    def instantiate(self):
        # Create an instance of the associated model using the fields stored in the version
        model_class = self.content_type.model_class()
        instance = model_class()

        for field_name, field_value in self.fields_snapshot.items():
            field = model_class._meta.get_field(field_name)
            print(field)
            if isinstance(field, models.ManyToManyField):
                # For ManyToMany fields, handle them separately
                self.instantiate_many_to_many(instance, field_name, field_value)
            elif isinstance(field, models.ForeignKey):
                # For ForeignKey fields, retrieve the related model instance
                related_model = field.related_model
                print(related_model)
                print("Foreign Key", field_name, field_value)
                try:
                    #kwargs = {to_field: field_value}
                    #related_instance = related_model.objects.get(**kwargs)
                    related_instance = related_model.objects.get(pk=field_value) #we cannot use pk = field value. we have to use a dynamic field
                    print(related_instance)
                    setattr(instance, field_name, related_instance)
                except related_model.DoesNotExist:
                    print("RElated no dey")  # Handle the case where the related instance does not exist
                # except Exception as e:
                #     print(f"{e.args}")
            elif isinstance(field, models.UUIDField):
                # For UUID fields, convert the string back to UUID
                print("UUID field", field_name, field_value)
                setattr(instance, field_name, uuid.UUID(field_value))
            else:
                # For other field types, set the value directly
                setattr(instance, field_name, field_value)

        print("DONE INSTANTIATING")
        return instance
    
    def instantiate_many_to_many(self, instance, field_name, field_value):
        # Handle ManyToMany fields
        field = instance._meta.get_field(field_name)
        related_model = field.related_model
        related_instances = related_model.objects.filter(pk__in=field_value)
        setattr(instance, field_name, related_instances)
    
    @property
    def _model(self):
        return self._content_type.model_class()
    
    @property
    def _content_type(self):
        return ContentType.objects.db_manager(self._state.db).get_for_id(self.content_type_id)

class PostVersion(VersionedModelMixin):
    pass
        

"""
from apis.models import *
user = User.objects.first()
post = Post.objects.first()

PostVersion.create_version(post, version_number=1, creator=user)
versions = PostVersion.objects.all()
"""