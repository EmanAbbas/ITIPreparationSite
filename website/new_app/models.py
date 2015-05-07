from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Track(models.Model):
	title=models.CharField(max_length=100)
	description=models.TextField(max_length=1200)

	def __str__():
		return self.title

class Question(models.Model):
	header=models.CharField(max_length=100)
	answer=models.TextField(max_length=1200)
	user_id=models.ForeignKey(User)
	track_id=models.ForeignKey(Track)

	def __str__():
		return self.header

class Material(models.Model):
	name=models.CharField(max_length=100)
	link=models.CharField(max_length=100)
	user_id=models.ManyToManyField(User)
	track_id=models.ManyToManyField(Track)

	def __str__():
			return self.name

class Type(models.Model):
	role = (
        ('HR', 'HR'),
        ('Technical', 'Technical'),
        ('Final','Final_interview') )
	role_type = models.CharField(max_length=1, choices=role)
	def __str__():
		return self.role_type


class Post(models.Model):
	title=models.CharField(max_length=100)
	body=models.TextField(max_length=1200)
	date=models.CharField(max_length=100)
	type_name=models.ForeignKey(Type)

	def __str__():
		return self.title