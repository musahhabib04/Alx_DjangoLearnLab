from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from .models import Post, Comment, Like
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404, Post
from .models import Post, Like
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def feed(request):
    user = request.user
    following_users = user.following.all()  # users the current user follows
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    post = generics.get_object_or_404(Post, pk=pk)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() 
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all() 
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        # Get posts authored by users the current user follows
        followed_users = user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')
    

class LikePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):
        user = request.user
        post = get_object_or_404(Post, pk=pk)

        # Prevent liking twice
        like, created = Like.objects.get_or_create(user=user, post=post)
        if not created:
            return Response({'detail': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)

        # Create notification for post owner (skip if actor == recipient)
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb='liked your post',
                target_content_type=ContentType.objects.get_for_model(post),
                target_object_id=post.pk
            )

        return Response({'detail': 'Post liked'}, status=status.HTTP_201_CREATED)

class UnlikePostAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, format=None):
        user = request.user
        post = get_object_or_404(Post, pk=pk)
        try:
            like = Like.objects.get(user=user, post=post)
        except Like.DoesNotExist:
            return Response({'detail': 'Like does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        # Delete notification(s) that match this like (optional)
        Notification.objects.filter(
            recipient=post.author,
            actor=user,
            verb__icontains='liked',
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.pk
        ).delete()

        like.delete()
        return Response({'detail': 'Unliked'}, status=status.HTTP_200_OK)

        
