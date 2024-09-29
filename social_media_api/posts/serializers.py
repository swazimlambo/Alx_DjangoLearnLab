from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comment, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']

    def validation(self, data):
        if not data['content'].strip():
            raise serializers.ValidationError({'content': 'Comment content cannot be empty'})
    
    def validate_content(self, value):
        if len(value) > 2000:
            raise serializers.ValidationError('Comment content is too long')
        
class PostSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fileds = ['id', 'author', 'content', 'created_at']