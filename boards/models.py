from email import message
from django.db import models
from django.contrib.auth.models import User

# Models represents Entities [or tables] in a DB

class Board(models.Model):
    board_pk = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    desc = models.CharField(unique=False, max_length=150)


class Topic(models.Model):
    topic_pk = models.IntegerField(primary_key=True)
    subject: models.CharField(max_length=150)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # to store date & time:
    # time_created = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    post_pk = models.IntegerField(primary_key=True)
    message = models.CharField(max_length=150)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

