from rest_framework import generics

from .models import User
from .serializers import UserSerializer


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
    serializer_class = UserSerializer

    # This method is used to overide the django create method embedded in the create api view
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        # this is used to grab the details cominig in from the frontend
        username = serializer.validated_data.get('username')
        print(username)
        serializer.save()
