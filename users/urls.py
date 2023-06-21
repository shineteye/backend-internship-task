from django.urls import path
from .views import UserDetailView, CreateUserView, UserListView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),
    path('create/', CreateUserView.as_view()),
    path('list/', UserListView.as_view()),
]
