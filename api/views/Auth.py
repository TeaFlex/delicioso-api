from rest_framework_simplejwt.views import TokenObtainPairView
from api.serializers.AuthSerializer import AuthSerializer

class AuthView(TokenObtainPairView):
    serializer_class = AuthSerializer