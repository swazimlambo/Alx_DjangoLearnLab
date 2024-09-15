from django import forms 
from django.contrib.auth.models import User, Comment
from django.contrib.auth.forms import UserCreationForm, ModelForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')

class CommentForm(forms.ModelForm):
    model = Comment
    fields = ('content')
