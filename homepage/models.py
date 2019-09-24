from django.db import models

# Create your models here.
class home_main_img(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

    class Meta:
        managed = True
        db_table = 'home_main_img'
        app_label = 'homepage'
