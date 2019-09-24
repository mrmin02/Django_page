from django.urls import path
from . import views

urlpatterns = [
    path('',views.new_music,name='new_music'),
    path('addmusic/',views.add_music,name='add_music')
]