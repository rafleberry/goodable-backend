from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(to=User)


class Post(models.Model):
    mux_playback_id = models.CharField(max_length=200)
    mp4_url = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)
    posted_date = models.DateTimeField()
