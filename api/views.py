from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from .models import User, Entry
from .serializers import UserSerializer


def get_users(request):
    users = User.objects.all().order_by("?").first()
    data = {}
    if users:
        data['id'] = users.id
        data['username'] = users.username
        data['email'] = users.email
    # serializer = UserSerializer(users, many=True)
    return JsonResponse({'users': data}, safe=False)


class UsersView(APIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        users = User.objects.all()
        return users

    def get(self, request, *args, **kwargs):
        users = self.get_queryset()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UsersViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        users = User.objects.all()
        return users
