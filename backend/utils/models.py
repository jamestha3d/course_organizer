from django.db import models
from django.utils.timezone import now
import uuid


#version mixin
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import json
from django.utils.functional import cached_property
from django.core.serializers.json import DjangoJSONEncoder
import uuid
from django.utils.timezone import now
from django.core.exceptions import ValidationError
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

    class STATUS(models.TextChoices):
        ACTIVE = 'active'
        DELETED = 'deleted'
        INACTIVE = 'inactive'
        BANNED = 'banned'
        OTHER = 'other'

    status = models.CharField(max_length=16, blank=True, null=True, default=STATUS.ACTIVE, choices=STATUS.choices)

    

    # def save(self, *args, **kwargs):
    #     """
    #     On save, update timestamps
    #     """
    #     if not self.created:
    #       self.created = now() #probably do not need this
    #     self.modified = now()

    #     return super().save(*args, **kwargs)
    
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





class ValidateTextChoice:
    def __init__(self, choices):
        self.choices = choices

    def __call__(self, value):
        """Validate that the value is in the defined choices."""
        if value not in self.choices:
            raise ValidationError(f'Value "{value}" is not a valid choice. Valid choices are: {[choice[0] for choice in self.choices]}')