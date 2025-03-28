from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from rest_framework import status, viewsets
from django.http import (
    Http404, HttpResponse, HttpRequest, HttpResponseRedirect, HttpResponseServerError, JsonResponse
)
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.contrib.sites.shortcuts import get_current_site



@csrf_exempt
def index(request):
    email_body = {
        "message": "This is a test email from Course Organizer App. Django Email Implemenation success",
        "title":  "Test email from Course Organizer",
        "email": ["jamestha3d@gmail.com"]   
    }
    
    message = email_body['message']
    email = email_body['email']
    title = email_body['title']
    send_mail(
        title, #title
        message, #message
        settings.EMAIL_HOST_USER, #sender if not available considered,
        email, #list of receivers
        fail_silently=False)
    return Response('email sent!')

class CustomThrottleClass(UserRateThrottle):
    rate = '5/minute'

class EmailView(APIView):
    throttle_classes = [CustomThrottleClass, AnonRateThrottle]
    def get(self, request, *args, **kwargs):
        from urllib.parse import urlparse
        print(request.scheme)
        print(get_current_site(request).domain)
        host = request.META.get('HTTP_HOST', '')
        host_dict = {key:str(value) for key,value in request.META.items()}
        from django.http import JsonResponse
        # host = dict(host)
        absolute_uri = request.build_absolute_uri()
        print(absolute_uri)
        # Parse the URI to extract components
        parsed_uri = urlparse(absolute_uri)

        # Extract the domain
        domain = parsed_uri.netloc

        # Scheme (http or https)
        scheme = parsed_uri.scheme

        # Path
        path = parsed_uri.path
        # response1 = {"message": 'This is a GET request', 'domain': domain, 'scheme': scheme, 'path': path, 'host': host, 'meta': request.META}
        # return Response(host)
        return JsonResponse(host_dict, json_dumps_params={'indent': 2}, safe=False)
        

    def post(self, request, *args, **kwargs):
        message = request.data['message']
        email = request.data['email']
        title = request.data['title']
        send_mail(
            title, #title
            message, #message
            settings.EMAIL_HOST_USER, #sender if not available considered,
            email, #list of receivers
            fail_silently=False)
        return Response({"message": "This is a POST request"})
    