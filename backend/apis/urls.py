#from django.conf.urls import url, include
from django.urls import include, re_path
from . import views
from django.urls import path

urlpatterns = [
    path("index/", views.index, name="apis_home"),
    re_path(r'^api/assignment/(?P<assignment_id>[0-9]+)/history/$', views.assignment_history, name='assignment-history'),
    path("assignment/<uuid:assignment_id>", views.assignment_history, name='assignments_history'),
    re_path(r'^assignment/version/(?P<version_id>[0-9]+)/$', views.assignment_version, name='assignment-version'),
]