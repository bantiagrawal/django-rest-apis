from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import pagination
from .models import HistoryPriceView, LatestPriceView
from .serializers import HistoryPriceViewSerializer, LatestPriceViewSerializer
from rest_framework.pagination import PageNumberPagination
from .filters import LatestPriceViewFilter,HistoryPriceViewFilter
from collections import OrderedDict
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
    filter_class = HistoryPriceViewFilter
    pagination_class=CustomPageNumberPagination
