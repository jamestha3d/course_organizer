from django.contrib import admin
from .models import Course, Assignment
from reversion.admin import VersionAdmin
# Register your models here.


admin.site.register(Assignment)
admin.site.register(Course)

# @admin.register(Course)

# class CourseAdmin(admin.ModelAdmin):
#     list_display=['title', 'created']
#     list_filter=['created']

# @admin.register(Assignment)
# class AssignmentModelAdmin(VersionAdmin):
#     pass

