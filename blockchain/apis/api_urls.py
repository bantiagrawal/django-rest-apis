from django.urls import path
from rest_framework import urlpatterns
from .views import LatestPriceViewset, HistoryPriceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('latestprice',LatestPriceViewset,basename='latestprice')
router.register('histprice',HistoryPriceViewSet,basename='histprice')
urlpatterns = router.urls