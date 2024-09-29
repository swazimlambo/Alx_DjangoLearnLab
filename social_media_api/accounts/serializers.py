from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomUser 
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_picture', 'followers', 'following']

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only = True)

    class Meta:
        model = CustomUser 
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_data']:
            raise serializers.ValidationError({'confirm_password': 'Password do not match'})
        return data

    def create(self, validate_data):
        del validate_data['confirm_password']    
        return CustomUser.objects.create_user(**validate_data)

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    passwork = serializers.CharField(write_only = True)

    def validate(self, data):
        user = CustomUser.objects.get(username = data['username'])
        if not user.check_password(data['password']):
            raise serializers.ValidationError({'password': 'Invalid password'})
        self.validated_data['user'] = user
        return data
    
class TokenSerializer(serializers.ModelsSerializers):
    class Meta:
        model = Token
        fields = ['key']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =['id', 'username', 'email', 'first_name']

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'following']

Token.objects.create
get_user_model().objects.create_user