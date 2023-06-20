from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from users.models import User
from users.serializers import UserSerializer
from django.forms.models import model_to_dict


@api_view(["GET"])
def get_users(request):
    # users = User.objects.all().order_by("?").first()
    instance = User.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data['id'] = users.id
        # data['username'] = users.username
        # data['email'] = users.email
        # serializer = UserSerializer(users, many=True)
        # data = model_to_dict(
        #     users, fields=["id", "is_superuser", "date_joined", "username", "email"])
        data = UserSerializer(instance)
    return JsonResponse({'users': data}, safe=False)


@api_view(["POST"])
def add_users(request, *args, **kwargs):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save()
        print(serializer.data)
        data = serializer.data
        return Response(data)
    return Response("Hello")


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
