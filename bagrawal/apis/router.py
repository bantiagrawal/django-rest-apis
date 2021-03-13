from .models import HistoryPriceView, LatestPriceView
ROUTED_MODELS = [HistoryPriceView, LatestPriceView]

class DBRouter(object):

    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'default'
        return None
