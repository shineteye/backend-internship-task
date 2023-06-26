from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import get_users, add_users, UsersView, UsersViewset

urlpatterns = [
    path('auth/', obtain_auth_token),
    # path('users/', get_users),
    # path('users/create/', add_users)
]
