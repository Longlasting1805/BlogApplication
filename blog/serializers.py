from rest_framework import serializers

from .models import BlogModel


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'content', 'author', 'date']

# class commentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['comment', 'post']
