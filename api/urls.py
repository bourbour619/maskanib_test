from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import IndexViewSet

router = DefaultRouter()
router.register(r'indexes', IndexViewSet, basename='index')

urlpatterns = [
    path('', include(router.urls))
]