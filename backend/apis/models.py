from django.db import models
from utils.models import GUIDModel
# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=256)
    
    @classmethod
    def get_domain_from_request_host(cls, request_host):
        return [s for s in request_host.split('.') if s != 'www'][0] if request_host else None
    pass

class Assignment(models.Model):
    pass

class Subject(models.Model):
    pass


