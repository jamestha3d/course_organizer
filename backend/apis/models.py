from django.db import models
from utils.models import GUIDModel
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.
import reversion

User = get_user_model()

class Course(GUIDModel): #AKA classroom
    title = models.CharField(max_length=256)
    code = models.CharField(max_length=6, blank=True, null=True)
    #students = models.ManyToManyField()
    
    
    @classmethod
    def get_domain_from_request_host(cls, request_host):
        return [s for s in request_host.split('.') if s != 'www'][0] if request_host else None
    

@reversion.register()
#register to use reversion with api. run python manage.py createinitialrevisions
class Assignment(GUIDModel):
    title = models.CharField(max_length=256)
    subject = models.ForeignKey('Subject', related_name='assignments', on_delete=models.CASCADE)
    due = models.DateTimeField()
    
    def __str__(self) -> str:
        return f"{self.subject} Assignment: {self.title}"
    

class Subject(GUIDModel):
    title = models.CharField(max_length=256)
    course = models.ForeignKey(Course, related_name='assignments', on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    
    def __str__(self) -> str:
        return f"{self.title} {self.code}"

class Submission(GUIDModel):
    pass
class Discussion(GUIDModel):
    pass

class Post(GUIDModel):
    content = models.TextField(max_length=1000)
    poster = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name="posts")
    likes = models.IntegerField(default=0)
    likers = models.ManyToManyField('Profile', blank=True, related_name="posts_liked")

    def __str__(self):
        return f" \n Post: {self.content} by {self.poster} \n  {self.likers.all().count()} likes"

    def num_likes(self):
        return self.likers.all().count()

    pass

class PostComment(GUIDModel):
    pass

class Comment(GUIDModel):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_made")
    content = models.CharField(max_length=200)
    #date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.poster)


class Profile(GUIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #image = models.ImageField(default='default.jpg', upload_to='profile_pics')


class Student(GUIDModel):
    pass

class Teacher(GUIDModel):
    pass