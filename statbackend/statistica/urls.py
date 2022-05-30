from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StatViewSet

router = DefaultRouter()
router.register('info', StatViewSet, basename='info')

urlpatterns = router.urls