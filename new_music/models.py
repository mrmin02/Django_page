from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # username = models.ForeignKey(User,to_field="username",on_delete=models.CASCADE,related_name="post_username",default="temp")
    title = models.CharField(max_length=30, null=False)
    content = models.TextField()
    youtube_id = models.CharField(max_length=30, null=False)
    singer = models.CharField(max_length=30)
    musical_composer = models.CharField(max_length=30)
    count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def update_counter(self):
        self.count = self.count + 1
        self.save()

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    # username = models.ForeignKey(User,to_field="username",on_delete=models.CASCADE,related_name="comment_username",default="temp")
    creater = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    comment = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
