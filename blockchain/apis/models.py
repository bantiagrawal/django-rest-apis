from django.db import models

class Employee(models.Model):
    name  = models.CharField(max_length =50, null=False)
    id = models.PositiveIntegerField(primary_key=True)
    dept = models.CharField(max_length =50)
    salary = models.PositiveIntegerField()
    create_ts = models.DateTimeField(auto_now_add=True)
    modified_ts = models.DateTimeField(auto_now_add=True)