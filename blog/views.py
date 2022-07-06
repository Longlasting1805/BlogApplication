from django.shortcuts import render
from rest_framework import viewsets

from .models import Post, Comment
from .serializers import BlogSerializer, CommentSerializer


# Create your views here.

class BlogView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
