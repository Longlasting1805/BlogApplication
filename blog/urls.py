from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogView, CommentView

router = DefaultRouter()
router.register('blogposts', BlogView, basename='blogposts')
router.register('comments', CommentView, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    # path('blogposts/', BlogView.as_view())
]
