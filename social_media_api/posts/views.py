
# Create your views here.

from django.shortcuts import render
from rest_framework import viewsets, pagination, filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import generics, status
from notifications.models import Notification
from .models import Comment, Post, Like
from .serializers import CommentSerializer, PostSerializer

class SetPagination(pagination.PageNumberPagination):
    page_size = 20
    page_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = SetPagination
    filter_backends = [filters.SearchFilter]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = SetPagination
    filter_backends = [filters.SearchFilter]

class PostFeedView(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    pagination_class = SetPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_query(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        if Like.objects.filter(post=post, user=user).exists():
            return Response({'detail': 'You have already liked this post'}, status = status.HTTP_400_BAD_REQUEST)
        
        Like.objects.get_or_create(user=request.user, post=post)
        Notification.objects.create(
            recipient = post.author,
            actor = user,
            verb = 'liked',
            target = post
        )
        return Response({'detail': 'Post liked successfully'}, status = status.HTTP_201_CREATED)
    
class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def delete(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user
        like = Like.objects.filter(user=user, post=post).first()

        if not like:
            return Response({'detail': 'You have not like this post'}, status = status.HTTP_400_BAD_REQUEST)
        
        like.delete()
        return Response({'detail': 'Post unliked successfully'}, status = status.HTTP_200_OK)