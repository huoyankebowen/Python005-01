from django.db import models
from datetime import datetime

# Create your models here.

class Order(models.Model):
    Order_id = models.AutoField(primary_key=True)
    Product = models.CharField(max_length=1000, blank=True, null=True)
    Created_time = models.DateTimeField(verbose_name="创建日期", default=datetime.now)
    User = models.CharField(max_length=50, blank=True, null=True)
    Canceld = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = u'Order'
        

