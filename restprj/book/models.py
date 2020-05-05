from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class BookModel(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    author = models.CharField(max_length=30)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
