from django.shortcuts import render

# Create your views here.
def new_music(req):
    return render(req,'new_music.html')
def add_music(req):
    return render(req,'add_music.html')