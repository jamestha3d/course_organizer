from django.conf import settings
from django.utils import timezone
from datetime import datetime
from re import sub

from django.db import connection
from django.conf import settings
import os

from rest_framework.authtoken.models import Token

# from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.contrib.auth.middleware import get_user
from django.utils import timezone
from django.core.cache import cache
from .models import Course, Assignment

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
        print('call to api')
        response = self.get_response(request)

        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        self.start_time = timezone.now()
    
    def process_template_response(self, request, response):
        print('process_template_response')

        #add context to request
        if settings.DEBUG:
            response.context_data['website'] = self.website
            response.context_data['website']['response_time'] = timezone.now() - self.start_time
        
        return response
    

class PortalMiddleware(object):
    """
    Middleware to detect the incoming hostname and take a specified action based
    on its value.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def get_course(self, request):
        """
        Returns an organization matching the domain from the request host. Only returns
        the organization if the authenticated user is in the list of members for that
        broker. Otherwise, returns a 404.
        """
        org = None

        if 'HTTP_HOST' in request.META:
            key = f'{request.META["HTTP_HOST"]}_org_object'
            org = cache.get(key)
            if not org:
                namespace = Course.get_domain_from_request_host(request.META['HTTP_HOST'])
                org = (
                    Course.objects.filter(namespace=namespace)
                    .prefetch_related('owner', 'owner__user')
                    .first()
                )
                #cache.set(key, org, 60 * 60 * 24)
        return org

    def get_location(self, request):
        """
        Returns an organization matching the domain from the request host. Only returns
        the organization if the authenticated user is in the list of members for that
        broker. Otherwise, returns a 404.
        """
        location = None
        namespace = None

        if 'HTTP_HOST' in request.META:
            if 'OTO-LOCATION' in request.headers:
                namespace = request.headers['OTO-LOCATION']
                try:
                    location = Assignment.objects.get(namespace=namespace)
                except Assignment.DoesNotExist:
                    pass
        return location

    def __call__(self, request, *args, **kwargs):
        # request.user = SimpleLazyObject(lambda: self.get_jwt_user(request))
        # header_token = request.META.get('HTTP_AUTHORIZATION', None)
        # if header_token:
        #     try:
        #         token = sub('Token ', '', request.META.get('HTTP_AUTHORIZATION', None))
        #         token_obj = Token.objects.get(key=token)
        #         request.user = token_obj.user
        #
        #     except Token.DoesNotExist:
        #         pass

        # set the site into the request for use in the project views
        request.org = self.get_course(request)
        request.location = self.get_location(request)
        response = self.get_response(request)
        return response

