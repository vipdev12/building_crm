from django.urls import path, include
from rest_framework import routers
from .views import ApartmentViewSet, ApartmentFilterView

router = routers.DefaultRouter()
router.register(r'apartments', ApartmentViewSet, basename='apartment')

urlpatterns = [
    path('', include(router.urls)),
    path('apartments/status/<str:status>/', ApartmentFilterView.as_view())
]