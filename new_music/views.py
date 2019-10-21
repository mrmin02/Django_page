from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Post, Comment
from django.core.exceptions import ObjectDoesNotExist  # except

from django.views.decorators.csrf import csrf_exempt
# from django.contrib import messages #use message


import json

# Create your views here.
def new_music(req): # this menu of main
    movies = Post.objects.all()
    return render(req,'new_music.html',{'movies':movies,'user':req.user})
def add_music(req):# move add_music page    // login
    if req.user.is_anonymous: # if user logout
        # messages.error(req, 'Please login !!')
        return redirect('/login/')
    return render(req,'add_music.html')



## add new music 
@csrf_exempt 
def create_music(req):  
    if req.method == 'POST':
        #user_id = req.user   -- ForeignKey assigned User    // not user.id 
        post = Post.objects.create(
            user_id = req.user.id,title = req.POST['title'],
            content = req.POST['content'], youtube_id = req.POST['youtube_id'],
            singer = req.POST['singer'], musical_composer = req.POST['musical_composer'],
            )
        return redirect('new_music')


## get item 

def show_item(req, item_id):#params item_id is urls.py  // name must ==
    #search in DB
    item = Post.objects.get(id=item_id)
    comment = Comment.objects.filter(post_id=item_id)        
    # print(comment)
    # user_name = User.objects.get()
    return render(req,'item_music.html',{'item':item,'comment':comment})
    # return HttpResponse(comment)


## modify post item
@csrf_exempt
def modify_item(req,item_id): ## put   but html only  get or post
    item = Post.objects.get(id=item_id)
    if req.user.id != item.user_id:
        return redirect('main')
    
    if req.method != "POST":
        return render(req,'add_music.html',{'item':item})
    item.youtube_id = req.POST['youtube_id']
    item.title = req.POST['title']
    item.singer = req.POST['singer']
    item.musical_composer = req.POST['musical_composer']
    item.content = req.POST['content']
    item.save()

    #redirect only string    item_id is int 
    return redirect('/music/item/'+str(item_id))


## remove post item
@csrf_exempt   
def remove_item(req,item_id):    
    item = Post.objects.get(id=item_id)
    item.delete()
    return redirect('new_music')


## add_comment
@csrf_exempt  
def add_comment(req,item_id):
    if req.method !="POST":
        return redirect('new_music')
    Comment.objects.create(
        comment = req.POST['comment'],
        creater_id=req.user.id, # why req.user.id ??  / when post create  req.user  ok  // after ..only req.user.id  ok.. why?
        post_id=item_id
    )
    # username = req.user.username
    return redirect('/music/item/'+str(item_id))


## modify_comment         html  only   GET   or  POST
@csrf_exempt
def modify_comment(req,item_id,comment_id):  
    if req.method !="POST":
        return redirect('/music/item/'+str(item_id))
    comment = Comment.objects.get(id=comment_id)  # input tag   is   made for click evenet listener   // so, post['input tag id '] is not found
    comment.comment = req.POST['new_comment'+str(comment_id)]
    comment.save()
    return redirect('/music/item/'+str(item_id))
    # return HttpResponse(req.POST)

@csrf_exempt
def delete_comment(req,item_id,comment_id):
    if req.method != "POST":
        return redirect('/music/item/'+str(item_id))

    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('/music/item/'+str(item_id))
