from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post, Comment

from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def new_music(req):
    movies = Post.objects.all()
    return render(req,'new_music.html',{'movies':movies})
def add_music(req):
    return render(req,'add_music.html')

@csrf_exempt  # add new music 
def create_music(req):
    if req.method == 'POST':
        #user_id = req.user   -- ForeignKey assigned User    // not user.id 
        post = Post.objects.create(
            user_id = req.user,title = req.POST['title'],
            content = req.POST['content'], youtube_id = req.POST['youtube_id'],
            singer = req.POST['singer'], musical_composer = req.POST['musical_composer'])
        return redirect('new_music')

