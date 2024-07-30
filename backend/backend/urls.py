"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apis.o_auth import OAuth2CallbackView
from apis.chat_gpt import authorize
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apis.urls")),
    path("auth/", include("accounts.urls")),
    path("emails/", include("emails.urls")),
    # path('authorize/', authorize, name='authorize'),
    path('oauth2callback/', OAuth2CallbackView.as_view(), name='oauth2callback'),
]
