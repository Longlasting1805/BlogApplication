from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200,
                             null=True)
    content = models.CharField(max_length=200,
                               null=True)
    author = models.CharField(max_length=100,
                              null=True)
    date = models.DateTimeField(auto_now_add=True,
                                null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.CharField(max_length=300,
                               blank=True)
    post = models.ForeignKey(Post, max_length=200, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True,
                                null=True)

    def __str__(self):
        return self.comment


