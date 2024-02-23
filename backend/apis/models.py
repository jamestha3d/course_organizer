from django.db import models
from utils.models import GUIDModel
from django.utils import timezone
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField #from django-autoslug
# Create your models here.
import reversion

#version mixin

from django.utils.timezone import now

User = get_user_model()
class Classroom(GUIDModel): #AKA classroom
    #this is a classroom. an overall topic. e.g french.
    title = models.CharField(max_length=256)
    namespace = AutoSlugField(populate_from='title', blank=True, null=True, editable=True, always_update=False)
    instructor = models.ForeignKey('Profile', on_delete=models.DO_NOTHING, null=True)
    description = models.TextField(null=True)
    
    # class Meta:
    #     unique_together = (('title', 'tagname', 'tagvalue'),)
    @classmethod
    def get_domain_from_request_host(cls, request_host):
        return [s for s in request_host.split('.') if s != 'www'][0] if request_host else None
    
    def __str__(self):
        return f'{self.title} - {self.description}'

class Assignment(GUIDModel):
    title = models.CharField(max_length=256)
    course = models.ForeignKey('Course', related_name='assignments', on_delete=models.CASCADE)
    due_date = models.DateTimeField(default=now, blank=True, null=True)
    description = models.TextField(null=True)
    #submissions = models.ManyToManyField('Submission', related_name='assignment')
    
    def __str__(self) -> str:
        return f"{self.course} Assignment: {self.title}"
    
class Submission(GUIDModel):
    assignment = models.ForeignKey('Assignment', on_delete=models.CASCADE, related_name='submission', null=True)
    attachments = models.ManyToManyField('Post')
    title = models.CharField(max_length=256)
    body = models.TextField()
    GRADES = (
            ('PASS', 'PASS'),
            ('FAIL', 'FAIL'),
            ('EXCELLENT', 'EXCELLENT'),
            ('VERY GOOD', 'VERY GOOD'),
            ('NOT GRADED', 'NOT GRADED'),
            )
    grade = models.CharField(max_length=10, choices=GRADES, default='NOT GRADED')
    student = models.ForeignKey('Profile', on_delete=models.DO_NOTHING, null=True)
    

class Course(GUIDModel):
    #this is a particular course. e.g french101 - speaking
    title = models.CharField(max_length=256)
    classroom = models.ForeignKey(Classroom, related_name='assignments', on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)
    namespace = AutoSlugField(populate_from='title', blank=True, null=True, editable=True, always_update=False)
    #students = models.ManyToManyField('Profile', related_name='Courses_registered', null=True)
    #instructors = models.ManyToManyField('Profile', related_name='Courses_teaching', null=True)
    description = models.TextField(null=True)
    
    def __str__(self) -> str:
        return f"{self.title} {self.code}"
    
class Session(GUIDModel):
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField(default=now)
    students = models.ManyToManyField('Profile', related_name='Courses_registered', through='StudentSession', through_fields=('session','student'))
    instructors = models.ManyToManyField('Profile', related_name='Courses_teaching')

class StudentSession(GUIDModel):
    session = models.ForeignKey('Session', on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)

class Cohort(GUIDModel):
    #session is for one course, cohort is for multiple courses. 
    #if students join a cohort, they will automatically be subscribed to every course in the cohort.
    courses = models.ManyToManyField('Course')
    start_date = models.DateTimeField(default=now)
    students = models.ManyToManyField('Profile', related_name='Cohorts_registered')
    instructors = models.ManyToManyField('Profile', related_name='Cohorts_teaching')


class Discussion(GUIDModel):
    pass

class Post(GUIDModel):
    content = models.TextField(max_length=1000)
    poster = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="posts")
    likes = models.ManyToManyField('Profile', blank=True, related_name="posts_liked")
    
    def __str__(self):
        return f" \n Post: {self.content} by {self.poster} \n  {self.likes.all().count()} likes"

    def num_likes(self):
        return self.likes.all().count()

class PostComment(GUIDModel):
    pass

class Comment(GUIDModel):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_made")
    content = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    likes = models.ManyToManyField('Profile')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.poster)


class Profile(GUIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLES = (
        ('STUDENT', 'STUDENT'),
        ('TEACHER', 'TEACHER')
        )
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    roles = models.CharField(
        max_length=255, default='STUDENT', choices=ROLES
    )
    img = models.ImageField(null=True, blank=True, default='default.jpeg')

    class Meta:
        ordering = ['created']

    def join_session(self, session: Session):
        if not session:
            return False
        if self not in session.students:
            session.students.add(self)
        return True
    
class Lesson(GUIDModel):
    title = models.CharField(max_length=256)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lessons')
    video_link = models.URLField()
    description = models.TextField()
    instructor = models.ManyToManyField(Profile, related_name='lessons', through='LessonInstructor', through_fields=('lesson', 'instructor'))
    assignments = models.ManyToManyField(Assignment, related_name='assignments' )

class LessonInstructor(GUIDModel):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    instructor = models.ForeignKey('Profile', on_delete=models.CASCADE)
    lead = models.BooleanField()

class Playlist(GUIDModel):
    title = models.CharField(max_length=256)
    lessons = models.ManyToManyField('Lesson', through='LessonPlaylist', through_fields=('playlist', 'lesson'))


class LessonPlaylist(GUIDModel):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    playlist = models.ForeignKey('Playlist', on_delete=models.CASCADE)
    number = models.IntegerField()
