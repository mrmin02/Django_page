# Generated by Django 2.2.3 on 2019-10-14 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment0',
            new_name='comment',
        ),
    ]