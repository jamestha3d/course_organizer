from django.db import models
from utils.models import GUIDModel
from django.utils import timezone
from django.contrib.auth import get_user_model
from autoslug import AutoSlugField #from django-autoslug
from django.core.validators import URLValidator, MaxValueValidator, MinValueValidator
import datetime
# Create your models here.
import reversion
from django.core.exceptions import ValidationError
#version mixin

from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from colorfield.fields import ColorField

User = get_user_model()

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

    def join_session(self, session: 'Session'):
        if not session:
            return False
        if self not in session.students:
            session.students.add(self)
        return True


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
    body = models.TextField(null=True, blank=True)
    author = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True)


class Institution(GUIDModel):
    name = models.CharField(max_length=256, blank=True, null=True, help_text="Name of Institution")
    brand_logo = models.ImageField(upload_to="institution_logos/", null=True, blank=True, help_text="Institution Logo")
    slug = AutoSlugField(populate_from='name', null=True, editable=True, always_update=False, help_text="institutions unique subdomain namespace") # TODO Add validator to ensure that slug is unique
    description = models.TextField(default='', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    
    class TYPE(models.TextChoices):
        INDIVIDUAL = 'individual', _('individual')
        SCHOOL = 'school', _('school')
        GOVT = 'government', _('government')

    def type_validator(value):
        if value not in Institution.TYPE.values:
            raise ValidationError(f'{value} is not a valid institution type. Choose from {", ".join([choice for choice in Institution.TYPE.values])}.')
    type = models.TextField(default=TYPE.INDIVIDUAL, choices=TYPE.choices, validators=[type_validator])
    country = models.CharField(max_length=255, blank=True, null=True)
    default_language = models.CharField(max_length =255, blank=True, null=True, default='english')
    currency = models.CharField(max_length=16, default='CAD', null=True, blank=True)
    brand_primary_color = ColorField(default='#FF0000', help_text="Primary color", null=True, blank=True)
    brand_secondary_color = ColorField(default='#FFFF00', help_text="Secondary color for buttons", null=True, blank=True)
    brand_tertiary_color = ColorField(default='#FFFFFF', help_text="backup color", null=True, blank=True)

    # class Meta:
    #     unique_together = ('student', 'session')
    #     ordering = ['-created']


class Program(GUIDModel):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', null=True, editable=True, always_update=False, help_text="Program unique slug")
    short_description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    cost = models.IntegerField()
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True, blank=True)
    public = models.BooleanField(default=True)
    image = models.ImageField(upload_to="programs/")
    duration = models.PositiveIntegerField(help_text="Estimated length of weeks to complete program.", null=True, blank =True)

class Course(GUIDModel):
    title = models.CharField(max_length=255)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

class Session(GUIDModel):
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True)
    institution = models.ForeignKey(Institution, null=True, blank=True, on_delete=models.SET_NULL)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    maximum_students = models.PositiveIntegerField(null=True, blank=True)
    # is_open = models.BooleanField(default=True) #This should be a dynamic property calculated on whether application deadline has passed? or start date
    description = models.TextField(null=True, blank=True)

    @property
    def is_open(self):
        if self.deadline:
            return now() < self.deadline
        return True
class StudentEnrollment(GUIDModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='enrollments')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='student_enrollments')
    payment_info = models.CharField(max_length=16, default='Trial')

    class Meta:
        unique_together = ('student', 'session')
        ordering = ['-created']

class InstructorEnrollment(GUIDModel):
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions_enrolled', validators=[])
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='instructor_enrollments')
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    enrolled_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True) #This should be auto filled so we can track the admin who enrolled the instructor

    def clean(self):
        super().clean()
        if not self.instructor.role == User.ROLES.INSTRUCTOR:
            raise ValidationError(f'The user {self.instructor} must have role of instructor before being enrolled as instructor')
        
    class Meta:
        unique_together = ('instructor', 'session')
        ordering = ['-created']
class Lesson(GUIDModel):
    title = models.CharField(max_length=255, null=True, blank=True, default='Lesson')
    index = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='lessons')
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons')
    
class LessonAttendance(GUIDModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    join_time = models.DateTimeField(null=True, blank=True)
    leave_time = models.DateTimeField(null=True, blank=True)

    @property
    def duration(self):
        if self.join_time and self.leave_time:
            return self.leave_time - self.join_time
        return None
class Assignment(GUIDModel):
    title = models.CharField(default='Lesson Assignment', max_length=255)
    description = models.TextField(null=True, blank=True)
    attachment = models.URLField(null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    max_score = models.PositiveIntegerField(default=100) # TODO validators=[MaxValueValidator(100)] dynamically set by institution

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['lesson', 'title']
class AssignmentSubmission(GUIDModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    # date = models.DateTimeField(auto_now_add=True)
    attachment = models.URLField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    score = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(100)])
    feedback = models.TextField(null=True, blank=True)
    class SUBMISSION_STATUS(models.TextChoices):
        SUBMITTED = 'submitted'
        GRADED = 'graded'
        LATE = 'late'

    submission_status = models.CharField(max_length=10, default=SUBMISSION_STATUS.SUBMITTED, choices=SUBMISSION_STATUS.choices)

    class Meta:
        unique_together = ('student', 'assignment')
        ordering = ['-created']
class Meeting(GUIDModel):
    title = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, related_name='meetings', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    meeting_link = models.URLField(validators=[URLValidator()])
    recorded_video = models.URLField(null=True, blank=True,)
    transcript = models.URLField(null=True, blank=True)
    is_recurring = models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])
    is_cancelled = models.BooleanField(default=False, choices=[(True, 'Yes'), (False, 'No')])
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='hosted_meetings')

    def __str__(self):
        return self.title