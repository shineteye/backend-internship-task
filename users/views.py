from rest_framework import generics

from .models import User
from .serializers import UserSerializer, CreateUserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # detail views usually get only one item
    # lookup_field = 'pk' by default


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    # This method is used to overide the django create method embedded in the create api view
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        # this is used to grab the details cominig in from the frontend
        username = serializer.validated_data.get('username')
        print(username)
        serializer.save()


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

    # perform update -> 1:57:09 time in the 7 hr video

    # def perform_update(self, serializer):
    #     instance = serializer.save()
    #     if not instance.username:
    #         instance.username = serializer.validated_data.get("username")
    #     if not instance.email:
    #         instance.email = serializer.validated_data.get("email")
    #     if not instance.password:
    #         instance.password = serializer.validated_data.get("password")
    #     serializer.save()


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'
