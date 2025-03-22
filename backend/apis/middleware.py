from django.conf import settings
from django.utils import timezone
from datetime import datetime
from re import sub

from django.db import connection
from django.conf import settings
import os

from rest_framework.authtoken.models import Token
from django.utils.functional import SimpleLazyObject
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.middleware import get_user
from django.utils import timezone
from django.core.cache import cache
from .models import Course, Assignment
from rest_framework.response import Response
from django.shortcuts import redirect
from django.urls import reverse, resolve
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
class ApiMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.start_time = None
        self.website = {
            'url': 'https://example.com',
            'debug': settings.DEBUG,
            'response_time': None
        }

    def __call__(self, request):
        # print('call to api')
        # request.user = SimpleLazyObject(lambda: self.get_jwt_user(request))
        # jwt_auth = JWTAuthentication()
        # user, _ = jwt_auth.authenticate(request)
        # request.user = user #this might not be necessary i just need to check against the user and not necessarily request.user.
        
        # if request.user and not request.user.is_anonymous and request.user.is_authenticated and not request.user.is_activated and not request.user.is_superuser:
        #     resolver_match = resolve(request.path)
        #     view_name = resolver_match.view_name
        #     url_kwargs = resolver_match.kwargs
        #     uid64 = url_kwargs.get('uid64')
        #     token = url_kwargs.get('token')
        #     allowed_paths = [] #[reverse('login')] #fix bug for reverse path activate without params
        #     if request.path not in allowed_paths:
        #         return JsonResponse({'message': 'User must activate their account before accessing views'})
        #     else:
        #         print('allowed path') # return JsonResponse({'message': 'allowed path'})
        # else:
        #     print('activated user')
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        self.start_time = timezone.now()
    
    def process_template_response(self, request, response):
        print('process_template_response')

        #add context to request
        if settings.DEBUG:
            if response.context_data is not None:
                response.context_data['website'] = self.website
                response.context_data['website']['response_time'] = timezone.now() - self.start_time
                
        return response
