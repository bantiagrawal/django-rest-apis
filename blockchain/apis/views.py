from django.shortcuts import render
from rest_framework import viewsets
from .models import HistoryPriceView, LatestPriceView
from .serializers import HistoryPriceViewSerializer, LatestPriceViewSerializer

class LatestPriceViewset(viewsets.ModelViewSet):
    queryset=LatestPriceView.objects.all()
    serializer_class = LatestPriceViewSerializer
    

class HistoryPriceViewSet(viewsets.ModelViewSet):
    queryset=HistoryPriceView.objects.all()
    serializer_class = HistoryPriceViewSerializer    