from django.db import models
from django.utils.timezone import now
import uuid
from model_utils import FieldTracker #pip install django-model-utils


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(default=now, editable=True, null=True )
    modified = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.id:
          self.created = now()
        self.modified = now()

        return super().save(*args, **kwargs)
    

class GUIDModel(models.Model):
    """
    Mixin for providing a model with a unique GUID
    """
    guid = models.UUIDField(primary_key=True, max_length=40, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        """
        On save, update timestamps
        """
        if not self.created:
          self.created = now()
        self.modified = now()

        return super().save(*args, **kwargs)
    
    class Meta:
        abstract = True
    


class ExpandedBaseModel(BaseModel):
    """
    Expand the base model to allow for navigation back
    and forward between instances in the admin.
    """

    def next(self):
        try:
            return type(self).objects.get(pk=self.pk + 1)
        except type(self).DoesNotExist:
            return None

    def previous(self):
        try:
            return type(self).objects.get(pk=self.pk - 1)
        except type(self).DoesNotExist:
            return None

    class Meta:
        abstract = True

    #FIeld Tracker
    # class Post(models.Model):
    #     title = models.CharField(max_length=255)
    #     author = models.ForeignKey(Author)
    #     tracker = FieldTracker()