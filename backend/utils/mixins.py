from utils import models
class AuditModelMixin(models.GUIDModel):
    class Meta:
        abstract = True



from django.db import models
from utils.models import BaseModel
from utils.mixins import AuditModelMixin
from django.contrib.auth.models import AbstractUser

class Account(BaseModel, AuditModelMixin, AbstractUser):
    first_name = models.CharField(max_length=64,
                                  default='', blank=True)
    last_name= models.CharField(max_length=64, default='', blank=True)


class ModelVersionMixin:
    user = models.CharField()
    comment = models.CharField()
    version = models.CharField()

    def pre_save():
        pass