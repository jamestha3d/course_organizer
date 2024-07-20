from django.db import models
from utils.models import GUIDModel
from django.utils import timezone
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField #from django-autoslug
import datetime
# Create your models here.
import reversion

#version mixin

from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

User = get_user_model()
# class Classroom(GUIDModel): #AKA classroom
#     #this is a classroom. an overall topic. e.g french.
#     title = models.CharField(max_length=256)
#     namespace = AutoSlugField(populate_from='title', blank=True, null=True, editable=True, always_update=False)
#     instructor = models.ForeignKey('Profile', on_delete=models.DO_NOTHING, null=True)
#     description = models.TextField(null=True)
    
#     # class Meta:
#     #     unique_together = (('title', 'tagname', 'tagvalue'),)
#     @classmethod
#     def get_domain_from_request_host(cls, request_host):
#         return [s for s in request_host.split('.') if s != 'www'][0] if request_host else None
    
#     def __str__(self):
#         return f'{self.title} - {self.description}'

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
    class GRADES(models.TextChoices):
        PASS = 'PASS'
        FAIL = 'FAIL'
        EXCELLENT = 'EXCELLENT'
        VERY_GOOD = 'VERY GOOD'
        NOT_GRADED = 'NOT GRADED'

    grade = models.CharField(max_length=10, choices=GRADES.choices, default=GRADES.NOT_GRADED)
    student = models.ForeignKey('Profile', on_delete=models.DO_NOTHING, null=True)
    

class Course(GUIDModel):
    #this is a particular course. e.g french101 - speaking
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=6, unique=True)
    namespace = AutoSlugField(populate_from='title', blank=True, null=True, editable=True, always_update=False)
    description = models.TextField(null=True)
    instructors = models.ManyToManyField('Profile', related_name='courses_teaching')

    def add_instructor(self, instructor:'Profile'):
        if instructor.role != Profile.ROLES.INSTRUCTOR:
            raise Exception('Cannot add Non Instructor as instructor')
        
        self.instructors.add(instructor)
            
    def __str__(self) -> str:
        return f"{self.title} {self.code}"
    
class Session(GUIDModel):
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField(default=now)
    students = models.ManyToManyField('Profile', related_name='sessions_registered', through='StudentSession', through_fields=('session','student'))
    instructors = models.ManyToManyField('Profile', related_name='sessions_teaching')

    def __str__(self) -> str:
        return f"{self.start_date} {self.end_date}"
class StudentSession(GUIDModel):
    session = models.ForeignKey('Session', on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
    #extra things

class Classroom(GUIDModel): #This should be renamed to classroom
    '''
        session is for one course, classroom is for multiple courses. 
        if students join a classroom, they will automatically be subscribed to every course in the classroom.
        Classroom can be public or private. students will only be able to join private classrooms if they are sent a link. Creating a public classroom/ more than 1 classroom will be a premium feature?. joining more than 1 classroom at a time will  be a premium feature.
        Cohorts have been deprecated. a cohort will just be a classroom with start and end date.

    '''
    title = models.CharField(max_length=200)
    courses = models.ManyToManyField('Course')
    start_date = models.DateTimeField(default=now, null=True)
    end_date = models.DateTimeField(null=True)
    students = models.ManyToManyField('Profile', related_name='classrooms_registered')
    admins = models.ManyToManyField('Profile', related_name='classrooms_teaching') #maybe i should call this managers?
    public = models.BooleanField(default=True)

    def add_admin(self, admin:'Profile'):
        #pass
        if admin.role == Profile.ROLES.ADMIN:
            self.admins.add(admin)
        else:
            raise Exception('Cannot add Non Instructor as instructor')
    def add_student(self, student:'Profile'):
        self.students.add(student)


class Discussion(GUIDModel):
    pass

class Post(GUIDModel):
    content = models.TextField()
    poster = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="posts")
    likes = models.ManyToManyField('Profile', blank=True, related_name="posts_liked")
    
    def __str__(self):
        return f" \n Post: {self.content} by {self.poster} \n  {self.likes.all().count()} likes"

    def num_likes(self):
        return self.likes.all().count()

#LMS
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
    
    class ROLES(models.TextChoices):
        STUDENT = 'STUDENT', _('STUDENT')
        INSTURCTOR= 'INSTRUCTOR', _('INSTRUCTOR')
        ADMIN = 'ADMIN', _('ADMIN')
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    role = models.CharField(
        max_length=255, default=ROLES.STUDENT, choices=ROLES.choices
    )
    image = models.ImageField(null=True, blank=True, default='default.jpeg')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.role}: {self.user.email}"

    def join_session(self, session: Session):
        if not session:
            return False
        if self not in session.students:
            session.students.add(self)
        return True
    
class Lesson(GUIDModel):
    title = models.CharField(max_length=256)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lessons')
    video_link = models.URLField(null=True)
    meeting_link = models.URLField(null=True)
    start_time = models.DateTimeField(null=True)
    one_hour = datetime.time(1,0,0)
    duration = models.TimeField(default=one_hour, null=True)
    notes = models.ForeignKey('LessonNote', on_delete=models.CASCADE, null=True)
    description = models.TextField()
    instructor = models.ManyToManyField(Profile, related_name='lessons', through='LessonInstructor', through_fields=('lesson', 'instructor'))
    assignments = models.ManyToManyField(Assignment, related_name='assignments' )
    #track attendance

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

class CourseRegistration(GUIDModel):
    pass

class LessonNote(GUIDModel):
    title = models.CharField(max_length= 20)
    body = models.TextField()
    author = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)
