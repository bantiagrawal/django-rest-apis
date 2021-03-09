from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import LatestPriceView, HistoryPriceView

class LatestPriceViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LatestPriceView
        fields = '__all__'

class HistoryPriceViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HistoryPriceView
        fields = '__all__'
