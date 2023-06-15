from rest_framework import generics, status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
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


class LoginView(APIView):
    permission_classes = ()  # exempting the login view from permissions

    def post(self, request):
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
