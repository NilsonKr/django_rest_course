from rest_framework.routers import DefaultRouter
from .viewSets import PatientsViewSet

router = DefaultRouter()
router.register('patients',PatientsViewSet)

urlpatterns = router.urls