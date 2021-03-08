from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    dept = models.CharField(max_length=50)
    salary = models.IntegerField()
    create_ts = models.DateTimeField()
    modified_ts = models.DateTimeField()

    class Meta:
        db_table = 'apis_employee'
