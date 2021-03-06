from django.urls import path
from . import views

urlpatterns = [
    path('',views.new_music,name='new_music'),
    path('addmusic/',views.add_music,name='add_music'),
    path('addmusic/create_item/',views.create_music,name='create_music'),
    path('item/<int:item_id>',views.show_item,name="show_item"),
    path('modify/<int:item_id>',views.modify_item,name="modify_item"),
    path('remove/<int:item_id>',views.remove_item,name="remove_item"),
    path('item/<int:item_id>/add_comment',views.add_comment,name="add_comment"),
    path('item/<int:item_id>/modify_comment/<int:comment_id>',views.modify_comment,name="modify_comment"),
    path('item/<int:item_id>/delete_comment/<int:comment_id>',views.delete_comment,name="modify_comment"),
]
