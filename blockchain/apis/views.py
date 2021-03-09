from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import pagination
from .models import HistoryPriceView, LatestPriceView
from .serializers import HistoryPriceViewSerializer, LatestPriceViewSerializer
from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param='row'

class LatestPriceViewset(viewsets.ModelViewSet):
    queryset=LatestPriceView.objects.all()
    serializer_class = LatestPriceViewSerializer
    filterset_fields = ['currency']
    pagination_class=CustomPageNumberPagination
    

class HistoryPriceViewSet(viewsets.ModelViewSet):
    queryset=HistoryPriceView.objects.all()
    serializer_class = HistoryPriceViewSerializer
    filterset_fields=['id','currency']
