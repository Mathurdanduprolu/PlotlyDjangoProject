# stock/models.py
from django.db import models

class StockData(models.Model):
    timestamp = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return f"{self.timestamp} - {self.close}"
