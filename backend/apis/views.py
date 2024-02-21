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
from .models import Course, Assignment, Classroom, Lesson, User, Profile, Post, PostComment
from rest_framework import status, viewsets
from .serializers import ClassroomSerializer, CourseSerializer, LessonSerializer, ProfileSerializer, PostSerializer, PostCommentSerializer, AssignmentSerializer
# Create your views here.

@api_view(['GET'])
def index(request:Request):

    return TemplateResponse(request, "index.html", {
        "any_context_key": "any_context_value"
    })

@api_view(['GET'])
def homepage(request):
    response = {"message": "Hello World"}
    return Response(data=response, status=status.HTTP_200_OK )


class AssignmentView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    # def get_queryset(self):
    #     queryset = self.queryset
    #     return queryset

class CourseView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    # def get_queryset(self):
    #     queryset = self.queryset
    #     return queryset


class ClassroomView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    # def get_queryset(self):
    #     queryset = self.queryset
    #     return queryset
    
class ProfileView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    # def get_queryset(self):
    #     queryset = self.queryset
    #     return queryset

class PostView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    # def get_queryset(self):
    #     queryset = self.queryset
    #     return queryset
    
class PostCommentView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = PostCommentSerializer
    queryset = PostComment.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    # def get_queryset(self):
    #     queryset = self.queryset
    #     return queryset
    
class LessonView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    # def get_queryset(self):
    #     queryset = self.queryset
    #     return queryset