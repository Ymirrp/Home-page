from django.contrib.auth.models import User
from django.db import models


class Boards(models.Model):
    _userid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    color = models.CharField(max_length=6)
    date = models.DateTimeField()


class Cards(models.Model):
    _userid = models.ForeignKey(User, on_delete=models.CASCADE)
    _boardid = models.ForeignKey(Boards, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, null=False)
    desc = models.CharField(max_length=255)
    date = models.DateTimeField()
    priority = models.IntegerField(default=-1)
    is_deleted = models.BooleanField(default=False)


class DeletedCards(models.Model):
    _userid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=255)
    date = models.DateTimeField()
