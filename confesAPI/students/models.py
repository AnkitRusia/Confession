from django.db import models

# Create your models here.

class Student(models.Model):
    StudentId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, default='')
    branch = models.CharField(max_length=50)
    profilePicName = models.CharField(max_length=100, default="default.png")

class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    description = models.TextField(default="Post description")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    StudentId = models.IntegerField(null=True)
    image = models.CharField(max_length=150, default="img")
    likes = models.IntegerField(default=0)
    title = models.TextField(default="Title")
    

class Comment(models.Model):
    commentId = models.AutoField(primary_key=True)
    description = models.TextField(blank=True)
    postId = models.IntegerField(null=True)

