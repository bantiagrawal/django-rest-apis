import django_filters
from .models import HistoryPriceView, LatestPriceView

class LatestPriceViewFilter(django_filters.FilterSet):

    class Meta:
        model = LatestPriceView
        fields = ['currency']

class HistoryPriceViewFilter(django_filters.FilterSet):

    class Meta:
        model = HistoryPriceView
        fields = ['id', 'currency', 'price']        