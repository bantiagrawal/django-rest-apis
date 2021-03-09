from django.urls import path
from rest_framework import urlpatterns
from .views import LatestPriceViewset, HistoryPriceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('latest-prices',LatestPriceViewset,basename='latest-price')
router.register('history-prices',HistoryPriceViewSet,basename='history-price')
urlpatterns = router.urls