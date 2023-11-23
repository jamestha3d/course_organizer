from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.

def index(request:Request):

    return TemplateResponse(request, "index.html", {
        "any_context_key": "any_context_value"
        #because we are using context data in the middleware, we need to pass context {} to the response and access the context in the template
    })

def homepage(request:Request):
    response = {"message": "Hello World"}
    return Response(data=response, status=status.HTTP_200_OK )


# class Something:

#     serializer_class=
#     permission_classes = [IsAuthenticated]
#     queryset = Model.objects.all()