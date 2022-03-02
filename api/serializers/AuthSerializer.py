from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from api.serializers.User import UserSerializer

class AuthSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: User):
        token =  super().get_token(user)
        token['auth_user'] = UserSerializer(user).data
        return token
