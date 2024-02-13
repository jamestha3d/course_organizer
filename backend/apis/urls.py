#from django.conf.urls import url, include
from rest_framework import routers
from django.urls import include, re_path
from .views import index, PostCommentView, CourseView, AssignmentView, ClassroomView
from django.urls import path

router = routers.DefaultRouter()
router.register(r'courses',
                CourseView, 'course_view')
router.register(r'classrooms',
                ClassroomView, 'classrooms')
urlpatterns = [
    path("index/", index, name="apis_home"),
    path('', include(router.urls))
    #re_path(r'^api/assignment/(?P<assignment_id>[0-9]+)/history/$', views.assignment_history, name='assignment-history'),
    #path("assignment/<uuid:assignment_id>", views.assignment_history, name='assignments_history'),
    #re_path(r'^assignment/version/(?P<version_id>[0-9]+)/$', views.assignment_version, name='assignment-version'),
]