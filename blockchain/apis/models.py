from django.db import models
import datetime
class HistoryPriceView(models.Model):
    id = models.BigIntegerField(blank=True, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    rowid = models.BigIntegerField(blank=True, null=True)
    cmc_rank = models.BigIntegerField(blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    volume_24h = models.CharField(max_length=50, blank=True, null=True)
    market_cap = models.CharField(max_length=50, blank=True, null=True)
    load_date_time = models.DateTimeField(blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True)

    @property
    def days(self):
        return (self.latest_load_time.date() - datetime.datetime.now().date()).days
    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'history_price_view'
        ordering = ['cmc_rank']

class LatestPriceView(models.Model):
    rowid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    symbol = models.CharField(max_length=100, blank=True, null=True)
    slug = models.CharField(max_length=100, blank=True, null=True)
    num_market_pairs = models.CharField(max_length=50, blank=True, null=True)
    date_added = models.CharField(max_length=100, blank=True, null=True)
    max_supply = models.CharField(max_length=50, blank=True, null=True)
    circulating_supply = models.CharField(max_length=50, blank=True, null=True)
    total_supply = models.CharField(max_length=50, blank=True, null=True)
    platform = models.CharField(max_length=200, blank=True, null=True)
    cmc_rank = models.BigIntegerField(blank=True, null=True)
    last_updated = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    volume_24h = models.CharField(max_length=50, blank=True, null=True)
    percent_change_1h = models.CharField(max_length=50, blank=True, null=True)
    percent_change_24h = models.CharField(max_length=50, blank=True, null=True)
    percent_change_7d = models.CharField(max_length=50, blank=True, null=True)
    percent_change_30d = models.CharField(max_length=50, blank=True, null=True)
    market_cap = models.CharField(max_length=50, blank=True, null=True)
    price_last_updated = models.CharField(max_length=50, blank=True, null=True)
    load_date = models.DateField(blank=True, null=True)
    load_date_time = models.DateTimeField(blank=True, null=True)
    latest_load_time = models.DateTimeField(blank=True, null=True)
    currency = models.CharField(max_length=50, blank=True, null=True)

    @property
    def days(self):
        return (self.latest_load_time.date() - datetime.datetime.now().date()).days
    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'latest_price_view'
        ordering = ['cmc_rank']        