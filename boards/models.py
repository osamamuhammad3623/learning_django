from email import message
from django.db import models
from django.contrib.auth.models import User

# Models represents Entities [or tables] in a DB

# database simple schema: a board consists of many topics, each topic has its comments

class Board(models.Model):
    board_pk = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    desc = models.CharField(unique=False, max_length=150)


class Topic(models.Model):
    topic_pk = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    topic_desc = models.CharField(max_length=300, null=False, default="auto")
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_pk = models.AutoField(primary_key=True)
    message = models.CharField(max_length=150)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

