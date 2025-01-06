from .viewsSets import DoctorsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('doctors', DoctorsViewSet)

urlpatterns = router.urls
