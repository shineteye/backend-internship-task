from django.urls import path
from .views import get_users, add_users, UsersView, UsersViewset

urlpatterns = [
    path('users/', get_users),
    path('users/create/', add_users)
]
