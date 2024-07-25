from django.shortcuts import render
from django.template.response import TemplateResponse
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view, action, permission_classes
from reversion.models import Version
from django.db.models import F
from .models import Course, Assignment, Classroom, Lesson, User, Profile, Post, PostComment
from rest_framework import status, viewsets
from .serializers import ClassroomSerializer, ClassroomDetailSerializer, CourseSerializer, LessonSerializer, ProfileSerializer, PostSerializer, PostCommentSerializer, AssignmentSerializer
from django.shortcuts import get_object_or_404

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

    @action(
        detail=False,
        methods=['GET',],
        permission_classes=[],
        # url_path="tags/(?P<tagname>[^/.]+)",
    )
    def my_assignments(self, request):
        print(request.user)
        return Response(f'{request.user}')
class CourseView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    @action(
        detail=False,
        methods=['GET',],
        permission_classes=[],
        # url_path="tags/(?P<tagname>[^/.]+)",
    )
    def mycourses(self, request):
        user_classrooms = Classroom.objects.filter(students__user=request.user).distinct().values_list('courses', flat=True)
        user_courses = Course.objects.filter(guid__in=user_classrooms)
        pages = self.paginate_queryset(user_courses)

        if pages is not None:
            serializer = CourseSerializer(pages, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = CourseSerializer(pages, many=True)
            return Response(serializer.data)
        
class ClassroomView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    
    
class ProfileView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

class PostView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'
    
class PostCommentView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = PostCommentSerializer
    queryset = PostComment.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    
class LessonView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'


class ClassroomView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ClassroomSerializer
    queryset = Classroom.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    def retrieve(self, request, guid=None):
        classroom = self.get_object()
        return Response(ClassroomDetailSerializer(classroom, remove_fields=['students'], context={'request': request}).data)


    @action(
        detail=False,
        methods=['GET',],
        permission_classes=[],
    )
    def myclassrooms(self, request):
        user_classrooms = Classroom.objects.filter(students__user=request.user).distinct()
        pages = self.paginate_queryset(user_classrooms)

        if pages is not None:
            serializer = ClassroomSerializer(pages, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            serializer = ClassroomSerializer(pages, many=True)
            return Response(serializer.data)
        
    
    @action(
        detail=True,
        methods=['POST',],
        permission_classes=[],
    )
    def join(self, request, guid=None):
        classroom = self.get_object()
        user = request.user
        if user and not classroom.students.filter(user=user).exists():
            classroom.students.add(user.profile)
            return Response(ClassroomDetailSerializer(classroom, context={'request': request}).data, status=status.HTTP_201_CREATED)
        
        else:
            return Response({"error": "User already in classroom"}, status=status.HTTP_403_FORBIDDEN)

    @action(
        detail=True,
        methods=['POST',],
        permission_classes=[],
    )
    def leave(self, request, guid=None):
        classroom = self.get_object()
        user = request.user
        if user and classroom.students.filter(user=user).exists():
            classroom.students.remove(user.profile)
            return Response(ClassroomDetailSerializer(classroom, context={'request': request}).data, status=status.HTTP_201_CREATED)
    
        else:
            return Response({"error": "User not in classroom"}, status=status.HTTP_403_FORBIDDEN)
