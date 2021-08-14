from django.db import models


# Create your models here.


class Customers(models.Model):
    name = models.CharField(max_length=20)
    email=models.EmailField(max_length=200)
    phone = models.CharField(max_length=10)
    bal = models.FloatField()

class Transactions(models.Model):
    from_name = models.CharField(max_length=20)
    to_name = models.CharField(max_length=20)
    trans_amt = models.FloatField()