from django.db import models

from utils.models import GUIDModel

# Create your models here.

class EmailTemplate(GUIDModel):
    language = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    sender = models.CharField(max_length=80, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    type = models.ForeignKey('EmailTemplateType', on_delete=models.DO_NOTHING, blank=True, null=True)

class EmailTemplateType(GUIDModel):
    # Do i really need this? ## This might be better than creating a model textchoices for type
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)