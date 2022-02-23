from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated

from api.serializers.User import AdminUserSerializer, UserSerializer
from api.views.utils.permissions import IsOwnerOrAdmin
from api.views.utils.viewsets import AdministrableViewSet

from django.contrib.auth.models import User

class UserViewSet(AdministrableViewSet):

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        # There's more data for staff than regular users
        if(self.request.user.is_staff):
            return AdminUserSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        # Users can only retreive their own infos
        owner_actions = [
            'retrieve',
        ]
        if(self.action in owner_actions):
            self.permission_classes.append(IsOwnerOrAdmin)
        return super().get_permissions()
