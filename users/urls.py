from django.urls import path
from .apiviews import CreateUserView, ListUsersView, LoginView

urlpatterns = [
    path('', ListUsersView.as_view(), name='create-user'),
    path('create/', CreateUserView.as_view(), name='create-user'),
    path('login/', LoginView.as_view(), name='login')
]
