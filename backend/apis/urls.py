#from django.conf.urls import url, include
from rest_framework import routers
from django.urls import include, re_path
from .views import index, homepage, PostCommentView, CourseView, AssignmentView, ClassroomView, ProfileView, LessonView
from django.urls import path
from .o_auth import OAuth2CallbackView, OAuth2InitView

router = routers.DefaultRouter()
router.register(r'courses',
                CourseView, 'course_view')
router.register(r'classrooms',
                ClassroomView, 'classrooms')
router.register(r'assignments',
                AssignmentView, 'assignments')
router.register(r'profiles',
                ProfileView, 'profiles')
router.register(r'lessons',
                LessonView, 'lessons')
urlpatterns = [
    path("index/", homepage, name="apis_home"),
    path('', include(router.urls)),
    #re_path(r'^api/assignment/(?P<assignment_id>[0-9]+)/history/$', views.assignment_history, name='assignment-history'),
    #path("assignment/<uuid:assignment_id>", views.assignment_history, name='assignments_history'),
    #re_path(r'^assignment/version/(?P<version_id>[0-9]+)/$', views.assignment_version, name='assignment-version'),
    path('oauth2init/', OAuth2InitView.as_view(), name='oauth2init'),
    path('oauth2callback/', OAuth2CallbackView.as_view(), name='oauth2callback'),

]

#GET /oauth2callback/?state=wPA0Ih0dNWZ1lqfg1dwqlpPWattfh3&code=4/0AcvDMrBYMgbaWtedXU3ckhEmGrDL4MSVhvkewBiRMh4fZlhvfhRxyYDuFuEGPI_u5kO66g&scope=https://www.googleapis.com/auth/calendar.events