from django.contrib import admin
from .models import Course, Assignment, Classroom
from reversion.admin import VersionAdmin
# Register your models here.
@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
    list_display=['title', 'created']
    list_filter=['created']

@admin.register(Assignment)
class AssignmentModelAdmin(VersionAdmin):
    pass