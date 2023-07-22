from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import IndexViewSet, IndexHistoryList

router = DefaultRouter()
router.register(r'indexes', IndexViewSet, basename='index')

urlpatterns = [
    path('index-histories/<str:ins_code>/',
         IndexHistoryList.as_view(), name='index-history')
]


urlpatterns += router.urls
