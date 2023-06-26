from rest_framework import generics, authentication
from rest_framework.response import Response
from .models import Entry
from .serializers import EntrySerializer
from api.authentication import TokenAuthentication


class ListEntries(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication
    ]


class CreateEntriesView(generics.CreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication
    ]
