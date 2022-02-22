from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

class AdministrableViewSet(ModelViewSet):
    """
        A ModelViewSet that permits to unauthenticated users to read and admins to read and write by default.
        You can edit the `admin_actions` attribute to select other actions available only for admins.
    """

    admin_actions = [
        'create',
        'update',
        'partial_update',
        'destroy',
    ]

    def get_permissions(self):
        if(self.action in self.admin_actions):
            self.permission_classes = [IsAdminUser, *self.permission_classes]
        return super().get_permissions()
