from django.urls import path
from .views import ListEntries, CreateEntriesView


urlpatterns = [
    path('list/', ListEntries.as_view()),
    path('create/', CreateEntriesView.as_view()),
]
