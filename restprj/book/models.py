from django.db import models

from django.db import models
from django.contrib.auth.models import User

#
# class Genre(models.Model):
#     title = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.title


class Book(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # title = models.CharField(max_length=30)
    # text = models.TextField()
    # author = models.CharField(max_length=30)
    # publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    # data = models.DateTimeField(auto_now_add=True)
    # genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        super().save(**kwargs)


class Comment(models.Model):
    comment_book = models.ForeignKey(Book,
                                     on_delete=models.CASCADE,
                                     related_name="comment")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
