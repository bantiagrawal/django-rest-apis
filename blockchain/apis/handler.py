import os
import sys
from django.db import connection
from mixer.django.backends import mixer

class BlockChainHandler:
    '''select * From bcm1.latest_price_view;
    '''
    def __init__(self):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blockchain.settings')
        

    def my_custom_sql(self):
        with connection.cursor() as cursor:
            cursor.execute("select count(1) From bcm1.latest_price_view")
            row = cursor.fetchone()

        return row
    def create_data(self):
        for i in range(100):
            mixer.blend('apis.Employee')
