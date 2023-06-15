from django.urls import path
from .apiviews import CreateUserView, ListUsersView

urlpatterns = [
    path('', ListUsersView.as_view(), name='create-user'),
    path('create/', CreateUserView.as_view(), name='create-user')
]
