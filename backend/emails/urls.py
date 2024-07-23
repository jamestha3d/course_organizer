from .views import index, EmailView
from django.urls import path
from rest_framework import routers
from django.urls import include


urlpatterns = [
    path("index/", index, name="email_index"),
    path('email', EmailView.as_view(), name='email')
]