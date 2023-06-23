from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Entry
from .serializers import EntrySerializer
from .permissions import IsStaffEditorPermission


class ListEntries(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = [IsStaffEditorPermission]


class CreateEntriesView(generics.CreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
