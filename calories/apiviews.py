from users.permissions import *
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Calories
from .serializers import CaloriesSerializer


class CaloriesView(generics.ListAPIView):
    permission_classes = ()
    authentication_classes = ()
    queryset = Calories.objects.all()
    serializer_class = CaloriesSerializer


class CreateCaloriesEntry(APIView):
    permission_classes = [RegularUserPermission]
    authentication_classes = ()
    serializer_class = CaloriesSerializer
    queryset = Calories.objects.all()

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
