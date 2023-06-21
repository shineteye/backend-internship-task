from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UsersViewset

router = DefaultRouter()
router.register(r'users', UsersViewset, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    # path('api/', include('api.urls')),
    path('api/users/', include('users.urls')),
    path('api/entries/', include('entrys.urls')),
]
