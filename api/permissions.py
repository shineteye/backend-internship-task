from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class RegularUserPermission(permissions.BasePermission):
    """
    Custom permission to only allow regular users to CRUD on their owned records.
    """

    def has_permission(self, request, view):
        # Allow all SAFE methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if user is the owner of the record
        return view.kwargs.get('pk') == request.user.id


class UserManagerPermission(permissions.BasePermission):
    """
    Custom permission to only allow user managers to CRUD only users.
    """

    def has_permission(self, request, view):
        # Allow all SAFE methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if user is a user manager
        return request.user.is_staff and not request.user.is_superuser


class AdminPermission(permissions.BasePermission):
    """
    Custom permission to only allow admins to CRUD all records and users.
    """

    def has_permission(self, request, view):
        # Allow all SAFE methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if user is an admin
        return request.user.is_superuser

# Viewset for entries
