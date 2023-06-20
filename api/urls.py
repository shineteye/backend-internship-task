from django.urls import path
from .views import get_users, UsersView, UsersViewset

urlpatterns = [
    # path('', UsersView.as_view(), name='list-users')
    path('users/', get_users)
]
