from django.contrib import admin
from .models import Course, Assignment, Subject 
# Register your models here.
@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
    list_display=['title', 'created']
    list_filter=['created']