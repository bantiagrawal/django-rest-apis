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
    days = filters.NumberFilter(field_name='load_date_time', method='get_days', label="days")

    def __init__(self, *args, **kwargs):
        kwargs['data']._mutable = True
        if 'days' not in kwargs['data']:
            kwargs['data']['days'] = 3
        if 'id' not in kwargs['data']:
            kwargs['data']['id'] = 1
        kwargs['data']._mutable = False

        super(HistoryPriceViewFilter, self).__init__(*args, **kwargs)
    def get_days(self, queryset, field_name, value):
        return queryset.filter(load_date_time__gte=datetime.now()-timedelta(days=int(value)))

    class Meta:
        model = HistoryPriceView
        fields = ['id', 'currency', 'days']        