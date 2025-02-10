from rest_framework import permissions

class IsDoctor(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'doctor') and request.user.doctor
