from collections import OrderedDict

from django.shortcuts import render
from rest_framework import pagination, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .filters import HistoryPriceViewFilter, LatestPriceViewFilter
from .models import HistoryPriceView, LatestPriceView
from .serializers import HistoryPriceViewSerializer, LatestPriceViewSerializer


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param='rows'

class LatestPriceViewset(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=LatestPriceView.objects.all()
    serializer_class = LatestPriceViewSerializer
    filter_class = LatestPriceViewFilter
    pagination_class=CustomPageNumberPagination
    

class HistoryPriceViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    queryset=HistoryPriceView.objects.all()
    serializer_class = HistoryPriceViewSerializer
    filter_class = HistoryPriceViewFilter
    pagination_class=CustomPageNumberPagination
