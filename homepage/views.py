from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

from new_music.models import Post

from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
import json

# from django.shortcuts import redirect
# Create your views here.

def main(req):
    # return HttpResponse('dd')
    movies = Post.objects.values('youtube_id')
    if req.user.is_authenticated:
        return render(req,'main.html',{'user':req.user,'movies':movies})
    return render(req,'main.html',{'movies':movies})
    # return render(req,'main.html',{'id': data.id,'title': data.title,'content':data.content}) #templates 를 자동으로 찾음.

@csrf_exempt
def login(req):
    if req.user.is_authenticated:
        return redirect('main')

    if req.method == "POST":
        username = req.POST['userid']
        password = req.POST['password']
        user = auth.authenticate(req, username=username, password=password)
        if user is not None:
            auth.login(req, user)
            return redirect('main')
        else:
            return render(req,'login.html',{'error':'username or password is incorrect'})
    return render(req,'login.html')

@csrf_exempt
def register(req):
    if req.user.is_authenticated:
        return redirect('main')
    if req.method == "POST":
        if User.objects.filter(username=req.POST["username"]).exists():
            return render(req,'register.html',{'error':'ID already exists'})
        else:
            user = User.objects.create_user(
                username = req.POST["username"], password=req.POST["password"], email=req.POST["email"])
            auth.login(req,user)
            return redirect('main')
    return render(req,'register.html')

def logout(req):
    auth.logout(req)
    return redirect('main')
