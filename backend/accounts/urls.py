from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("activate/<str:uidb64>/<str:token>/", views.ActivationView.as_view(), name="activate"),
    path("send_activation/", views.SendActivationEmailView.as_view(), name="send_activation"),
    path("login/<str:uidb64>/<str:token>/", views.SingleSignOnView.as_view(), name="single_sign_on"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt-create"),
    path("jwt/refresh/", TokenRefreshView.as_view(),name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),

]