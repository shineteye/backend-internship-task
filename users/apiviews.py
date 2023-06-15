from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadonly, RegularUserPermission, UserManagerPermission, AdminPermission


class CreateUserView(generics.CreateAPIView):
    # using authentication_classes = () and permission_classes = () to exempt UserCreate from global authentication scheme.
    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class ListUsersView(generics.ListCreateAPIView):
    permission_classes = [UserManagerPermission, AdminPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUserDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [UserManagerPermission, AdminPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer
