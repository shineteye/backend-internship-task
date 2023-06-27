from rest_framework.routers import DefaultRouter

from entrys.viewsets import EntryViewSet

router = DefaultRouter()
router.register('Entrys', EntryViewSet, basename='entries')

urlpatterns = router.urls
