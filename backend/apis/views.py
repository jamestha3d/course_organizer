from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view
from reversion.models import Version
from django.db.models import F
from .models import Course, Assignment, Subject
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

@api_view()
def assignment_history(request:Request, assignment_id):
    assignment = Assignment.objects.get(guid=assignment_id)
    versions = Version.objects.get_for_object(assignment)

    data = versions.values('pk',
                           'revision__date_created',
                           'revision__user__username',
                           'revision__comment',
                           'pk')
    
    data = versions.values('pk',
                        date_time=F('revision__date_created'),
                        user=F('revision__user__username'),
                        comment=F('revision__comment'))
    
    return Response({'data': data})


@api_view()
def assignment_version(request, version_id):
    v = Version.objects.get(id=version_id)
    #Version.objects.get(id=15).revision.revert() to revert
    #v._object_version.object to get the instance of the object as it were
    
    return Response({"data": v.field_dict})