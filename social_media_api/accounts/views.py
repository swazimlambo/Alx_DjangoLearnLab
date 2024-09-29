from django.shortcuts import render, redirect
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from posts.models import Post
from .models import CustomUser
from .serializers import RegistrationSerializer, TokenSerializer, ProfileSerializer, LoginSerializer, FollowSerializer


# Create your views here.
class RegistrationView (generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            Token.objects.create(user = user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

class RegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer 

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            Token.objects.create(user = user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user = user)
            return Response({'token': 'token.key'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class TokenRetrieveView(generics.GenericAPIView):
    permission_classes = permissions.IsAuthenticated
    serializer_class = TokenSerializer

    def get(self, request):
        token = Token.objects.get(user = request.user)
        serializer = self.get_serializer(token)
        return Response(serializer.data)
    
class ProfileView(generics.GenericAPIView):
    serializer_class = ProfileSerializer

    def patch(self, request):
        user = request.user
        serializer = self.get_serializer(user, data = request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer

    def post(self, request, user_id):
        user_to_follow = CustomUser.objects.get(id = user_id)
        follower = request.user
        if follower == user_to_follow:
            return Response({'detail': 'You can not follow yourself'}, status = status.HTTP_400_BAD_REQUEST)
        
        if user_to_follow in follower.following.all():
            return Response({'detail': 'You already following this user'}, status = status.HTTP_400_BAD_REQUEST)
        
        follower.following.add(user_to_follow)
        return Response({'detail': 'You followed successfully'}, status = status.HTTP_201_CREATED)
    
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, user_id):
        user_to_unfollow = CustomUser.objects.get(id = user_id)
        follower = request.user

        if user_to_unfollow not in follower.following.all():
            return Response({'detail': 'You do not follow this user'}, status = status.HTTP_400_BAD_REQUEST)
        
        follower.following.remove(user_to_unfollow)
        return Response({'detail': 'User unfollowed successfully'}, status = status.HTTP_204_NO_CONTENT)

class FollowerListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer
    
    def get(self, request, user_id):
        user = CustomUser.objects.get(id = user_id)
        followers = user.followers.all()
        serializer = self.get_serializer(followers, many = True)
        return Response(serializer.data)
    
class FollowingListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer
    queryset = CustomUser.objects.all()

    def get(self, request, user_id):
        user = CustomUser.objects.get(id = user_id)
        following = user.following.all()
        serializer = self.get_serializer(following, many = True)
        return Response(serializer.data)