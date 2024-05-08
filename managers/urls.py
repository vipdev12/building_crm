from django.urls import path, include
from rest_framework import routers
from .views import ManagerViewSet

router = routers.DefaultRouter()
router.register(r'managers', ManagerViewSet, basename='manager')

urlpatterns = [
    path('', include(router.urls))
]