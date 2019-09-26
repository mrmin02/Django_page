from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post, Comment

from django.views.decorators.csrf import csrf_exempt
# from django.contrib import messages #use message


import json

# Create your views here.
def new_music(req):
    movies = Post.objects.all()
    return render(req,'new_music.html',{'movies':movies,'user':req.user})
def add_music(req):# move add_music page    // login
    if req.user.is_anonymous: # if user logout
        # messages.error(req, 'Please login !!')
        return redirect('/login/')
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
def show_item(req, item_id):#params item_id is urls.py  // name must ==
    #search in DB
    item = Post.objects.get(id=item_id)
    # post = Post.update_counter(Post)
    return render(req,'item_music.html',{'item':item})
