from django.contrib import admin
from .models import EmailTemplate, EmailTemplateType
# Register your models here.

admin.site.register(EmailTemplate)
admin.site.register(EmailTemplateType)