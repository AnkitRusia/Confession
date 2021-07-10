from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import Http404
from django.core.files.storage import default_storage
from django.conf import settings
import os
from PIL import Image

from students.models import Student, Post
from students.serializers import StudentSerializer, PostSerializer, CommentSerializer

# Create your views here.

@csrf_exempt
def studentAPI(request, id=0):
    if request.method == 'GET':
        students = Student.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)
    
    if request.method == 'POST':
        student_data = JSONParser().parse(request) 
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(f"Failed to add student : {student_serializer.errors}", safe=False)
    
    if request.method == 'PUT':
        student_data = JSONParser().parse(request) 
        student = Student.objects.get(StudentId=student_data["StudentID"])
        student_serializer = StudentSerializer(student, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(f"Updated Successfully", safe=False)
        return JsonResponse("Failed to update student", safe=False)
    
    if request.method == 'DELETE':
        student = Student.objects.get(StudentId=id)
        student.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def postAPI(request, id=0):
    if request.method == 'GET':
        posts = Post.objects.all()
        posts_serializer = PostSerializer(posts, many=True)
        return JsonResponse(posts_serializer.data, safe=False)
    
    if request.method == 'POST':
        name = request.GET.get("name", 'NoName')
        password = request.GET.get("password")
        try:
            student = Student.objects.get(name=name)
            if password != student.password:
                return JsonResponse("Wrong password", safe=False)
        except Student.DoesNotExist:
            raise Http404("Student not found")
        post_data = JSONParser().parse(request) 
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add post", safe=False)
    
    if request.method == 'PUT':
        name = request.GET.get("name", 'NoName')
        password = request.GET.get("password")
        try:
            student = Student.objects.get(name=name)
            if password != student.password:
                return JsonResponse(f"Wrong password {password} != {student.password}", safe=False)
        except Student.DoesNotExist:
            raise Http404("Student not found")
        post_data = JSONParser().parse(request) 
        post = Post.objects.get(postId=post_data["postId"])
        post_serializer = PostSerializer(post, data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to update student", safe=False)
    
    if request.method == 'DELETE':
        post = Post.objects.get(PostId=id)
        post.delete()
        return JsonResponse("Deleted Successfully", safe=False)

@csrf_exempt
def SaveStudentImage(request, id=0):
    file = request.FILES["sImg"]
    full_file_name = "Student//" + file.name
    file_name = default_storage.save(full_file_name, file)
    student = Student.objects.get(StudentId=id)
    img_path = os.path.join(settings.BASE_DIR, "media", student.profilePicName)
    os.remove(img_path)
    student.profilePicName = full_file_name
    img_path = os.path.join(settings.BASE_DIR, "media", student.profilePicName)
    img = Image.open(img_path)
    img = img.resize((250, 250))
    img.save(img_path)
    student.save(update_fields=['profilePicName'])
    return JsonResponse(f"Successfully Saved {file_name}", safe=False)

@csrf_exempt
def SavePostImage(request, id=0):
    file = request.FILES["pImg"]
    file_name = default_storage.save(file.name, file)
    post = Post.objects.get(PostId=id)
    img_path = os.path.join(settings.BASE_DIR, "media", post.image)
    os.remove(img_path)
    post.image = file_name
    post.save(update_fields=['image'])
    return JsonResponse(f"Successfully Saved {file_name}", safe=False)

@csrf_exempt
def viewPostByName(request):
    if request.method == 'GET':
        name = request.GET.get("name", 'NoName')
        try:
            student = Student.objects.get(name=name)
        except Student.DoesNotExist:
            raise Http404("Student not found")
        try:
            posts = Post.objects.filter(StudentId=student.StudentId)
            posts_serializer = PostSerializer(posts, many=True)
            return JsonResponse(posts_serializer.data, safe=False)
        except Post.DoesNotExist:
            raise Http404("Post not found")
        
@csrf_exempt
def likePost(request, id=0):
    if request.method == 'GET':
        post = Post.objects.get(postId=id)
        post.likes += 1
        post.save(update_fields=["likes"])
        return JsonResponse(f"Liked post with id = {id}", safe=False)
    return JsonResponse(f"Failed to find post with id= {id}", safe=False)

@csrf_exempt
def addComment(request):
    if request.method == 'POST':
        name = request.GET.get("name", 'NoName')
        password = request.GET.get("password")
        try:
            student = Student.objects.get(name=name)
            if password != student.password:
                return JsonResponse("Wrong password", safe=False)
        except Student.DoesNotExist:
            raise Http404("Student not found")

        comment_data = JSONParser().parse(request) 
        comment_serializer = CommentSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse("Comment Added Successfully", safe=False)
        return JsonResponse("Failed to add comment", safe=False)