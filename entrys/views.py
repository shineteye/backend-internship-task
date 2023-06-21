from rest_framework import generics
from rest_framework.response import Response
from .models import Entry
from .serializers import EntrySerializer


class ListEntries(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class CreateEntriesView(generics.CreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
