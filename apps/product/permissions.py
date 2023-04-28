from rest_framework import permissions


class ReadOnlyOrAdmin(permissions.BasePermission):
    """
    Custom permission to allow read-only access to all users, and full access only to admin users.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff