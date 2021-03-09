from django_filters import rest_framework as filters
from .models import HistoryPriceView, LatestPriceView
from datetime import datetime, timedelta

class LatestPriceViewFilter(filters.FilterSet):
    days = filters.NumberFilter(field_name='latest_load_time', method='get_days', label="days")
    def get_days(self, queryset, field_name, value):
        return queryset.filter(latest_load_time__gte=datetime.now()-timedelta(days=int(value)))
        
    class Meta:
        model = LatestPriceView
        fields = ['currency','days']

class HistoryPriceViewFilter(filters.FilterSet):
    days = filters.NumberFilter(field_name='latest_load_time', method='get_days', label="days")

    def get_days(self, queryset, field_name, value):
        return queryset.filter(latest_load_time__gte=datetime.now()-timedelta(days=int(value)))

    class Meta:
        model = HistoryPriceView
        fields = ['id', 'currency', 'days']        