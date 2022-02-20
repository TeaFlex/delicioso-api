from rest_framework.permissions import BasePermission
from rest_framework.request import Request

class IsSuperUser(BasePermission):

    def has_permission(self, request: Request, view, *args, **kwargs):
        return bool(request.user and request.user.is_superuser)

class IsOwner(BasePermission):
    def has_object_permission(self, request: Request, view, obj, *args, **kwargs):
        return bool(obj.id == request.user.id)

class IsOwnerOrAdmin(IsOwner):
    def has_object_permission(self, request: Request, view, obj, *args, **kwargs):
        if(request.user.is_staff):
            return True
        return super().has_object_permission(request, view, obj, *args, **kwargs)