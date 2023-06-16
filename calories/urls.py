from django.urls import path
from .apiviews import CaloriesView, CreateCaloriesEntry

urlpatterns = [
    path('', CaloriesView.as_view(), name='list-entries'),
    path('create/', CreateCaloriesEntry.as_view(), name='create'),
]
