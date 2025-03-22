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
from .models import (
    Course, Assignment, Lesson, AssignmentSubmission, Meeting,
    Profile, Institution, Program, Session, StudentEnrollment, InstructorEnrollment)
from rest_framework import status, viewsets
from .serializers import (SessionSerializer, SessionDetailSerializer, CourseSerializer, LessonSerializer, ProfileSerializer, 
                        AssignmentSerializer, AssignmentSubmissionSerializer, MeetingSerializer, InstitutionSerializer,
                        ProgramSerializer, InstructorEnrollmentSerializer, StudentEnrollmentSerializer)
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
User = get_user_model()
# Create your views here.


@api_view(['GET'])
def index(request:Request):

    return TemplateResponse(request, "index.html", {
        "any_context_key": "any_context_value"
    })

@api_view(['GET'])
@swagger_auto_schema(
    operation_summary="Get Homepage",
    operation_description="This returns homepage"
)
def homepage(request):
    response = {"message": "Hello World"}
    return Response(data=response, status=status.HTTP_200_OK )


class AssignmentView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    # @action(
    #     detail=False,
    #     methods=['GET',],
    #     permission_classes=[],
    #     # url_path="tags/(?P<tagname>[^/.]+)",
    # )
    # def my_assignments(self, request):
    #     print(request.user)
    #     return Response(f'{request.user}')
    
class ProfileView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'
    
    # @action(permissoin)
    # def change_colors(self, request):
    #     return
    
    
class LessonView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'


class SessionView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SessionSerializer
    queryset = Session.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

    # def retrieve(self, request, guid=None):
    #     classroom = self.get_object()
    #     return Response(SessionDetailSerializer(classroom, remove_fields=['students'], context={'request': request}).data)


    # @action(
    #     detail=False,
    #     methods=['GET',],
    #     permission_classes=[],
    # )
    # def myclassrooms(self, request):
    #     user_classrooms = Session.objects.filter(students__user=request.user).distinct()
    #     pages = self.paginate_queryset(user_classrooms)

    #     if pages is not None:
    #         serializer = SessionSerializer(pages, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     else:
    #         serializer = SessionSerializer(pages, many=True)
    #         return Response(serializer.data)
        
    
    # @action(
    #     detail=True,
    #     methods=['POST',],
    #     permission_classes=[],
    # )
    # def join(self, request, guid=None):
    #     classroom = self.get_object()
    #     user = request.user
    #     if user and not classroom.students.filter(user=user).exists():
    #         classroom.students.add(user.profile)
    #         return Response(SessionDetailSerializer(classroom, context={'request': request}).data, status=status.HTTP_201_CREATED)
        
    #     else:
    #         return Response({"error": "User already in classroom"}, status=status.HTTP_403_FORBIDDEN)

    # @action(
    #     detail=True,
    #     methods=['POST',],
    #     permission_classes=[],
    # )
    # def leave(self, request, guid=None):
    #     classroom = self.get_object()
    #     user = request.user
    #     if user and classroom.students.filter(user=user).exists():
    #         classroom.students.remove(user.profile)
    #         return Response(SessionDetailSerializer(classroom, context={'request': request}).data, status=status.HTTP_201_CREATED)
    
    #     else:
    #         return Response({"error": "User not in classroom"}, status=status.HTTP_403_FORBIDDEN)

class ProgramView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

class InstitutionView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = InstitutionSerializer
    queryset = Institution.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

class MeetingView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

class AssignmentSubmissionView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = AssignmentSubmissionSerializer
    queryset = AssignmentSubmission.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

class CourseView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

class StudentEnrollmentView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = StudentEnrollmentSerializer
    queryset = StudentEnrollment.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'

class InstructorEnrollmentView(viewsets.ModelViewSet):
    permission_classes = []
    serializer_class = InstructorEnrollmentSerializer
    queryset = InstructorEnrollment.objects.all()
    filter_fields = '__all__'
    lookup_field = 'guid'