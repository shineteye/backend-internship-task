from rest_framework import generics
from api.mixins import IsOwnerOrReadOnlyPermissionMixin, UserQuerySetMixin
from .models import Entry
from .serializers import EntrySerializer


class ListEntries(UserQuerySetMixin, IsOwnerOrReadOnlyPermissionMixin, generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    # to change the user field i will just change the specify the user_field to something like owner
    # user_field = 'owner'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     request = self.request
    #     user = request.user
    #     print(request.user)
    #     if not user.is_authenticated:
    #         return Entry.objects.none()
    #     return queryset.filter(user=request.user)


class ListEntry(UserQuerySetMixin, IsOwnerOrReadOnlyPermissionMixin, generics.ListAPIView):
    serializer_class = EntrySerializer

    def get_queryset(self):
        queryset = Entry.objects.all()
        pk = self.kwargs.get('pk')
        if pk:
            queryset = queryset.filter(pk=pk)
        return queryset


class CreateEntriesView(UserQuerySetMixin, IsOwnerOrReadOnlyPermissionMixin, generics.CreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

    def get_queryset(self):
        queryset = super().get_queryset()
        request = self.request
        user = request.user
        print(request.user)
        if not user.is_authenticated:
            return Entry.objects.none()
        return queryset.filter(user=request.user)


class UpdateEntryView(IsOwnerOrReadOnlyPermissionMixin, generics.UpdateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
