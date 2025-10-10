from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView, LikePostAPIView, UnlikePostAPIView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path('posts/<int:pk>/like/', LikePostAPIView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', UnlikePostAPIView.as_view(), name='post-unlike'),
]

