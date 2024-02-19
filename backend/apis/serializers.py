from rest_framework import serializers
from utils.serializers import FlexibleSerializer
from .models import Course, Classroom, Lesson, Profile, Post, PostComment, Assignment

class ProfileSerializer(FlexibleSerializer):

    class Meta:
        read_only_fields = ('created',)
        model = Profile
        fields = '__all__'


class CourseSerializer(FlexibleSerializer):
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