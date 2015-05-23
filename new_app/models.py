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
    answer = models.TextField(max_length=1200)
    user_id = models.ForeignKey(User)
    track_id = models.ManyToManyField(Track)

    type = models.CharField(choices=type_choices, max_length=10, default='TRACK')



    def __str__(self):
        return self.header


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
    track_id = models.ManyToManyField(Track)


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