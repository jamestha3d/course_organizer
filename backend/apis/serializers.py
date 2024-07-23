from rest_framework import serializers
from utils.serializers import FlexibleSerializer
from .models import Course, Classroom, Lesson, Profile, Post, PostComment, Assignment

class ProfileSerializer(FlexibleSerializer):

    class Meta:
        read_only_fields = ('created',)
        model = Profile
        fields = '__all__'


class CourseSerializer(FlexibleSerializer):
    instructors = serializers.SerializerMethodField()

    def get_instructors(self, obj):
        return obj.instructors.values_list('user__email', flat=True)
    class Meta:
        read_only_fields = ('created',)
        model = Course
        fields = '__all__'


class ClassroomSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Classroom
        fields = '__all__'


class PostSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Post
        fields = '__all__'

class PostCommentSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = PostComment
        fields = '__all__'

class AssignmentSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Assignment
        fields = '__all__'


class ClassroomSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Classroom
        fields = '__all__'

class LessonSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Lesson
        fields = '__all__'

class CourseCodeSerializer(FlexibleSerializer):
    class Meta:
        model = Course
        fields = ('code',)
class ClassroomSerializer(FlexibleSerializer):
    class Meta:
        read_only_fields = ('created',)
        model = Classroom
        fields = '__all__'

class ClassroomDetailSerializer(FlexibleSerializer):
    # courses = CourseCodeSerializer(many=True)
    courses = serializers.SerializerMethodField()
    #instructors = serializers.SerializerMethodField()
    is_student = serializers.SerializerMethodField()
    # is_instructor = serializers.SerializerMethodField()
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
        model = Classroom
        fields = '__all__'