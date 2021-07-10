from rest_framework import serializers
from students.models import Student, Post, Comment
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('StudentId', 'name', 'branch', 'profilePicName', "password")
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('postId', 'description', 'date', 'StudentId', 'image')
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment