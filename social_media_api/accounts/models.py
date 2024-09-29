from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField()
    followers = models.ManyToManyField('self', symmetrical=False, related_name='users_following')
    following = models.ManyToManyField('self', symmetrical=False, related_name='user_to_follow')