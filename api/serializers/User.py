from pyexpat import model
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'last_login',
            'is_staff',
        ]

class AdminUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = [
            'password'
        ]