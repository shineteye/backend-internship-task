from .permissions import IsOwnerOrReadOnly, IsUserManager, IsAdmin


class IsOwnerOrReadOnlyPermissionMixin():
    permission_classes = [
        IsOwnerOrReadOnly
    ]


class IsManagerPermissionMixin():
    permission_classes = [
        IsUserManager
    ]


class IsAdminPermissionMixin():
    permission_classes = [
        IsAdmin
    ]


class UserQuerySetMixin():
    user_field = 'user'
    allow_staff = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        print(lookup_data)
        queryset = super().get_queryset(*args, **kwargs)
        if self.allow_staff and user.is_admin:
            return queryset
        if user.is_admin:
            return queryset
        return queryset.filter(**lookup_data)
