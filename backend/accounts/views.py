from django.shortcuts import render
from .serializers import SignUpSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage
from emails.utils import welcome_email
# Create your views here.

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
                # "user": user.email,
                "user": {
                    "email": user.email,
                    "activated": user.is_activated
                }
            }
            welcome_email(user)
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
                    "activated": user.is_activated
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
    

class SendActivationEmailView(APIView):
    def post(user, request):
        token = account_activation_token.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        domain = get_current_site(request).domain
        protocol = request.scheme #'https' if request.is_secure() else 'http' 
        activation_link = f"{protocol}://{domain}/activate/{uid}/{token}/"

        subject = 'Activate Your Account'
        message = render_to_string('emails/template_welcome_user.html', {
            'user': user,
            'activation_link': activation_link,
        })
        email = EmailMessage(subject, message, to=[user.email])
        email.send()
        return Response({'message': 'Activation link sent'})
    
class ActivationView(APIView):
    permission_classes = []
    def post(self, request, uidb64, token):
        '''
            This view will activate newly signed up userss
        '''
        User = get_user_model()
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except:
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_activated = True
            user.save()
            return Response()
        else:
            return Response('Activation link is invalid or expired!')
        

