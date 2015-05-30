from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SiteUser(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username


class Track(models.Model):
    title = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.title



class Question(models.Model):

    type_choices = (
        ('IQ', 'IQ'),
        ('EN', 'English'),
        ('FAQ', 'FAQ'),
        ('TRACK', 'Track'),
    )

    header = models.CharField(max_length=100)
    user_id = models.ForeignKey(User)
    track_id = models.ManyToManyField(Track, blank=True)

    type = models.CharField(choices=type_choices, max_length=10, default='TRACK')

    voteUpUsers = models.ManyToManyField(User, blank=True,related_name='questionUpVotes')
    voteDownUsers = models.ManyToManyField(User, blank=True,related_name='questionDownVotes')

    @property
    def votes(self):
        return self.voteUpUsers.count() - self.voteDownUsers.count()

    def __str__(self):
        return self.header

class Answer(models.Model):
    body = models.TextField("Answer")
    question_id = models.ForeignKey(Question)
    user_id = models.ForeignKey(User)

    def __str__(self):
        return self.body

class Material(models.Model):

    type_choices = (
        ('IQ', 'IQ'),
        ('EN', 'English'),
        ('TRACK', 'Track'),
    )

    name = models.CharField(max_length=100)
    link = models.URLField()
    type = models.CharField(choices=type_choices, max_length=10, default='TRACK')

    description = models.TextField(blank=True)
    user_id = models.ForeignKey(User)
    track_id = models.ManyToManyField(Track, blank=True)


    def __str__(self):
        return self.name


class Type(models.Model):
    role = (
        ('HR', 'HR'),
        ('Technical', 'Technical'),
        ('Final', 'Final_interview') )
    role_type = models.CharField(max_length=1, choices=role)

    def __str__(self):
        return self.role_type


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=1200)
    date = models.CharField(max_length=100)
    type_name = models.ForeignKey(Type)

    def __str__(self):
        return self.title