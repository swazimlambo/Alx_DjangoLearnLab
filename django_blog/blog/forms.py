from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, ModelForm
from .models import Comment, Post
from taggit.forms import TagWidget as Widget
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {'tags': TagWidget()}
