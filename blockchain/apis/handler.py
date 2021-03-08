from django.db import connection

class BlockChainHandler:
    '''select * From bcm1.latest_price_view;
    '''
    def __init__(self):
        pass

    def my_custom_sql(self):
        with connection.cursor() as cursor:
            cursor.execute("select count(1) From bcm1.latest_price_view")
            row = cursor.fetchone()

        return row

bc_handler = BlockChainHandler()
count = bc_handler.my_custom_sql()

print(count)