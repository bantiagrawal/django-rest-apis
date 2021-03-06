from datetime import datetime, timedelta

from django_filters import rest_framework as filters

from .models import HistoryPriceView, LatestPriceView


class LatestPriceViewFilter(filters.FilterSet):        
    class Meta:
        model = LatestPriceView
        fields = ['currency']

class HistoryPriceViewFilter(filters.FilterSet):
    days = filters.NumberFilter(field_name='load_date_time', method='_days', label="days")

    def __init__(self, *args, **kwargs):
        kwargs['data']._mutable = True
        if 'days' not in kwargs['data']:
            kwargs['data']['days'] = 3
        if 'id' not in kwargs['data']:
            kwargs['data']['id'] = 1
        kwargs['data']._mutable = False
        super(HistoryPriceViewFilter, self).__init__(*args, **kwargs)
    
    def _days(self, queryset, field_name, value):
        return queryset.filter(load_date_time__gte=datetime.today().date()-timedelta(days=int(value)))
    class Meta:
        model = HistoryPriceView
        fields = ['id', 'currency', 'days']        
