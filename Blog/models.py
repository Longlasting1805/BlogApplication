from django.db import models


# Create your models here.

class BlogModel(models.Model):
    title = models.CharField(max_length=200,
                             null=True)
    content = models.CharField(max_length=200,
                               null=True)
    author = models.CharField(max_length=100,
                              null=True)
    date = models.DateTimeField(auto_now_add=True,
                                null=True, blank=True)


