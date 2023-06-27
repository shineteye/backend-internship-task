from django.urls import path
from .views import ListEntries, ListEntry, CreateEntriesView


urlpatterns = [
    path('create/', CreateEntriesView.as_view()),
    path('list/', ListEntries.as_view(),),
    path('list/<int:pk>/', ListEntry.as_view(), name='entry-detail'),
    path('<int:pk>/update/', ListEntry.as_view(), name='entry-edit'),
    path('create/', CreateEntriesView.as_view()),
]
