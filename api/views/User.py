from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from api.serializers.User import AdminUserSerializer, UserSerializer
from api.views.utils.permissions import IsOwner
from api.views.utils.viewsets import AdministrableViewSet

class UserViewSet(AdministrableViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if(self.request.user.is_staff):
            return AdminUserSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        owner_actions = [
            'retrieve',
        ]
        if(self.action in owner_actions):
            self.permission_classes.append(IsOwner)
        return super().get_permissions()
