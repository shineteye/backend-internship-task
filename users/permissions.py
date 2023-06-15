from rest_framework import permissions


class IsOwnerOrReadonly(permissions.BasePermission):
    """
    creating permissions for only the owner of an object to have access to it
    adding permissions also for anyone also to make requests
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions to owner of the request
        return obj.owner == request.user


class RegularUserPermission(permissions.BasePermission):
    """
    Custom permission to allow only regular users CRUD on their records
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user is the owner of the record
        if view.kwargs.get('pk') == request.user.id:
            return True


class UserManagerPermission(permissions.BasePermission):
    """
    Custom permission to allow only managers CRUD only users 
    """

    def has_permission(self, request, view):
        # Allow all SAFE methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # check if user is a user manager
        if request.user.is_staff and not request.user.is_superuser:
            return True


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow all SAFE methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # check if the user is an admin
        if request.user.is_superuser:
            return True
