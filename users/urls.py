from django.urls import path
from .views import UserDetailView, CreateUserView, UserListView

urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view()),
    path('create/', CreateUserView.as_view()),
    path('list/', UserListView.as_view()),
]
