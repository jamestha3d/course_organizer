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
    attachments = models.ManyToManyField('Post') #foreign key on Post model or other attachment model instead?
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
    #is_active = models.BooleanField(default=True) #When a course is active you can can create new lessons. if it is inactive no lessons can be created.
    def add_instructor(self, instructor:'Profile'):
        if instructor.role != Profile.ROLES.INSTRUCTOR:
            raise Exception('Cannot add Non Instructor as instructor')
        
        self.instructors.add(instructor)
            
    def __str__(self) -> str:
        return f"{self.title} {self.code}"
    
class Session(GUIDModel):
    # Maybe classroom will be classroom of students and session will be a session that starts and ends. and classroom doesnt start and end. just like in a university.
    # The session starts. and we add courses to the session.?
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
    #assignments?
    #submissions?
    #extra things

class Classroom(GUIDModel): #This should be renamed to classroom
    '''
        session is for one course, classroom is for multiple courses. 
        if students join a classroom, they will automatically be subscribed to every course in the classroom.
        Classroom can be public or private. students will only be able to join private classrooms if they are sent a link. Creating a public classroom/ more than 1 classroom will be a premium feature?. joining more than 1 classroom at a time will  be a premium feature.
        Cohorts have been deprecated. a cohort will just be a classroom with start and end date.

    '''
    title = models.CharField(max_length=200)
    courses = models.ManyToManyField('Course') # TODO maybe courses should belong to only one classroom. that means we will change the unique code structure.
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

    def __str__(self):
        return f"{self.title} {self.start_date.date()}"


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
    # first_name = models.CharField(max_length=36, null=True) #
    # profile_image = models.ImageField(upload_to='profile_pics', null=True, blank=True, default='default.jpg')
    class ROLES(models.TextChoices):
        STUDENT = 'STUDENT', _('STUDENT')
        INSTRUCTOR = 'INSTRUCTOR', _('INSTRUCTOR')
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
    index = models.PositiveIntegerField() #editable=False?. I probably don't need index at all because i can sort by Date Created.
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lessons')
    notes = models.ForeignKey('LessonNote', on_delete=models.CASCADE, null=True)
    description = models.TextField()
    # instructor = models.ManyToManyField(Profile, related_name='lessons', through='LessonInstructor', through_fields=('lesson', 'instructor')) #This field should be on the course not the lesson.
    assignments = models.ManyToManyField(Assignment, related_name='assignments' )
    # TODO ??add a is_recurring field to track whether the meeting is recurring or not??. maybe i should abstract meeting link to its own Model, where meeting link.
    #track attendance
    # abstracting meeting into it's own model makes sense because Potentially we can make a lesson that is just Notes and No meeting at all.


    # On lesson creation...
    
class Meeting(GUIDModel): #Maybe called Meeting/Lecture
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='meeting')
    recording_upload = models.URLField(null=True)
    meeting_link = models.URLField(null=True)
    start_time = models.DateTimeField(null=True) #this should record only start time and not day. so that if the meeting is recurring it will always recurr at the exact time and we can calculate date by adding 7 to previous meeting day?
    one_hour = datetime.time(1,0,0)
    duration = models.TimeField(default=one_hour, null=True)
    is_recurring = models.BooleanField(default=False)
    transcript = models.TextField()
    description = models.TextField()

    #if meeting is recurring, override the create method and when you save the meeting, if the Classroom that the meeting belongs to has not ended, then it should create the next lesson.
    #will need to manage creation of next meeting link and mailing reminder to students. maybe with a cron job.

# Don't need this.
# class LessonInstructor(GUIDModel):
#     lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
#     instructor = models.ForeignKey('Profile', on_delete=models.CASCADE)
#     lead = models.BooleanField()

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


# When a classroom is created, courses can be added. registration link can be shared with students for them to sign up for the class. When the first lesson is created/ with meeting.
#(#students should choose whether or not to receive email notifications)
#When lesson is created. we want to send an email with it's meeting link to students.
#if the meeting is recurring. we want to send an email for next meeting link??? Do this later?
#User can set notifications for things like receive notification when video is uploaded. when lesson is created. etc. 