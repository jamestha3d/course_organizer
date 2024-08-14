#from django.conf.urls import url, include
from rest_framework import routers
from django.urls import include, re_path
from . import views
from django.urls import path
from .o_auth import OAuth2CallbackView, OAuth2InitView

router = routers.DefaultRouter()
router.register(r'courses',
                views.CourseView, 'course_view')
router.register(r'assignments',
                views.AssignmentView, 'assignments')
router.register(r'profiles',
                views.ProfileView, 'profiles')
router.register(r'lessons',
                views.LessonView, 'lessons')
router.register(r'programs',
                views.ProgramView, 'programs')
router.register(r'institutions',
                views.InstitutionView, 'institutions')
router.register(r'sessions',
                views.SessionView, 'sessions')
router.register(r'student_enrollment',
                views.StudentEnrollmentView, 'student_enrollment')
router.register(r'instructor_enrollment',
                views.InstructorEnrollmentView, 'instructor_enrollment')

urlpatterns = [
    path('', include(router.urls)),
    # path('oauth2init/', OAuth2InitView.as_view(), name='oauth2init'),
    # path('oauth2callback/', OAuth2CallbackView.as_view(), name='oauth2callback'),

]

#GET /oauth2callback/?state=wPA0Ih0dNWZ1lqfg1dwqlpPWattfh3&code=4/0AcvDMrBYMgbaWtedXU3ckhEmGrDL4MSVhvkewBiRMh4fZlhvfhRxyYDuFuEGPI_u5kO66g&scope=https://www.googleapis.com/auth/calendar.events