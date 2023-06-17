from rest_framework import permissions
from rest_framework.views import Request, View


class IsAdminOrReadyOnly(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_authenticated and request.user.is_staff
        )


class IsObjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.username == request.user.username:
            return True
        return False
