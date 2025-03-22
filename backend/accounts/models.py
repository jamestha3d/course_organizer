from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.serializers.json import DjangoJSONEncoder
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email=self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff as True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser as True")
        
        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    # email=models.CharField(max_length=80)
    email = models.EmailField(max_length=80, unique=True) #models.EmailField(unique=False) maybe?
    username=models.CharField(max_length=45, null=True, unique=True)
    is_activated = models.BooleanField(default=False)
    objects=CustomUserManager()
    REQUIRED_FIELDS = [] #['username', 'first_name'] #['username']
    USERNAME_FIELD = "email"
    class GENDER(models.TextChoices):
        MALE = 'Male', _('Male')
        FEMALE = 'Female', _('Female')
        NEUTRAL = 'Neutral', _('Neutral')
        NON_BINARY = 'Non Binary', _('Non Binary')
        OTHER = 'Other', _('Other')
        NOT_SET = 'Not set', _('Not Set')
        # TODO add gender validator
    gender = models.CharField(max_length=12, default=GENDER.NOT_SET, choices=GENDER.choices)
    status = models.CharField(max_length=32, null=True, blank=True)
    institution = models.ForeignKey('apis.Institution', on_delete=models.CASCADE, blank=True, null=True)
    image = models.URLField(null=True, blank=True)
    google_tokens = models.JSONField(encoder=DjangoJSONEncoder, blank=True, null=True)
    zoom_tokens = models.JSONField(encoder=DjangoJSONEncoder, blank=True, null=True)
    class ROLES(models.TextChoices):
        STUDENT = 'STUDENT', _('STUDENT')
        INSTRUCTOR = 'INSTRUCTOR', _('INSTRUCTOR')
        ADMIN = 'ADMIN', _('ADMIN')
        SUPER_ADMIN = 'SUPER_ADMIN', _('SUPER_ADMIN')
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(
        max_length=255, default=ROLES.STUDENT, choices=ROLES.choices
    )
    class Meta:
        unique_together = ('institution', 'email')
    def __str__(self):
        return str(self.email)
    
    def clean(self):
        #TODO ensure that admin user has institution id
        pass
    