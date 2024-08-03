from rest_framework import serializers
from utils.serializers import FlexibleSerializer
from .models import (Course, Session, Lesson, Profile, Assignment,
                    Program, Meeting, AssignmentSubmission, LessonAttendance, 
                    Institution)

class ProfileSerializer(FlexibleSerializer):

    class Meta:
        read_only_fields = ('created',)
        model = Profile
        fields = '__all__'

class AssignmentSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Assignment
        fields = '__all__'


class SessionSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Session
        fields = '__all__'

class LessonSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Lesson
        fields = '__all__'

class SessionSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Session
        fields = '__all__'

class SessionDetailSerializer(FlexibleSerializer):
    courses = serializers.SerializerMethodField()
    is_student = serializers.SerializerMethodField()
    students_count = serializers.SerializerMethodField()
    def get_courses(self, obj):
        return list(obj.courses.values_list('title', flat=True))
    
    # def get_instructors(self, obj):
    #     return list(obj.instructors.values_list('', flat=True))

    def get_is_student(self, obj):
        if self.context and 'request' in self.context:
            user = self.context['request'].user
            return obj.students.filter(user=user).exists()
        return False
    
    # def get_is_instructor(self, obj):
    #     if self.context and 'request' in self.context:
    #         user = self.context['request'].user
    #         return obj.instructors.filter(user=user).exists()
    #     return False
    
    def get_students_count(self, obj):
        return obj.students.count()
    class Meta:
        read_only_fields = ('created',)
        model = Session
        fields = '__all__'

class MeetingSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Meeting
        fields = '__all__'

class ProgramSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Program
        fields = '__all__'

class AssignmentSubmissionSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = AssignmentSubmission
        fields = '__all__'

class LessonAttendanceSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = LessonAttendance
        fields = '__all__'

class CourseSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Course
        fields = '__all__'

class InstitutionSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Institution
        fields = '__all__'
