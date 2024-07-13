from django.shortcuts import render
from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []
    def post(self, request:Request):
        data = request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            user=serializer.save()
            tokens=create_jwt_pair_for_user(user)
            response={
                "message": "User Created Successfully",
                "token": tokens,
                #"data": serializer.data
                "user": user.email
            }
            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = []
    def post(self,request:Request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            tokens=create_jwt_pair_for_user(user)
            response={
                "message": "Login Successful",
                "token": tokens, #user.auth_token.key old token method,
                "user": {
                    "email": user.email,
                }

            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"errors": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request:Request):
        content = {
            "user": str(request.user),
            "auth": str(request.auth)
        }

        return Response(data=content, status=status.HTTP_200_OK)
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        token['email'] = user.email
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer