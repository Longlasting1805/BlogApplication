from django.shortcuts import render
from rest_framework import viewsets

from .models import BlogModel
from .serializers import BlogSerializer


# Create your views here.

class BlogView(viewsets.ModelViewSet):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
