from rest_framework import viewsets, generics
from rest_framework.response import Response
from knox.models import AuthToken
from .models import Entry, CustomUser
from .serializers import EntrySerializer, CustomUserSerializer, RegisterSerializer
from .permissions import IsOwnerOrReadOnly, RegularUserPermission, UserManagerPermission, AdminPermission


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [RegularUserPermission]

    def perform_create(self, serializer):
        # Automatically set user to current user on creation
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Return only entries owned by the current user, unless admin
        if self.request.user.is_superuser:
            return Entry.objects.all()
        else:
            return Entry.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [
                IsOwnerOrReadOnly, RegularUserPermission]
        else:
            self.permission_classes = [
                IsOwnerOrReadOnly, UserManagerPermission | AdminPermission]
        return super().get_permissions()


# Viewset for users


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AdminPermission]
        else:
            self.permission_classes = [UserManagerPermission | AdminPermission]
        return super().get_permissions()

# Register API


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": CustomUserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })
