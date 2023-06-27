from rest_framework import viewsets

from .models import Entry
from .serializers import EntrySerializer
from api.mixins import IsAdminPermissionMixin


class EntryViewSet(IsAdminPermissionMixin, viewsets.ModelViewSet):
    """
    The Viewset creates routes for the following
    get -> list -> QuerySet
    get -> retrieve -> Entry Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial Update
    delete -> destroy
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
