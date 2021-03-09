from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import pagination
from .models import HistoryPriceView, LatestPriceView
from .serializers import HistoryPriceViewSerializer, LatestPriceViewSerializer
from rest_framework.pagination import PageNumberPagination
from .filters import LatestPriceViewFilter,HistoryPriceView
class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param='rows'

class LatestPriceViewset(viewsets.ModelViewSet):
    queryset=LatestPriceView.objects.all()
    serializer_class = LatestPriceViewSerializer
    filter_class = LatestPriceViewFilter
    pagination_class=CustomPageNumberPagination
    

class HistoryPriceViewSet(viewsets.ModelViewSet):
    queryset=HistoryPriceView.objects.all()
    serializer_class = HistoryPriceViewSerializer
    filter_class = LatestPriceViewFilter
