from django.db import models

# Create your models here.

class Index(models.Model):
    ins_code = models.CharField(primary_key=True, max_length=20)
    lval30 = models.CharField(max_length=25)

class IndexHistory(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True)
    low = models.DecimalField(max_digits=8, decimal_places=1, blank=True)
    high = models.DecimalField(max_digits=8, decimal_places=1, blank=True)
    close = models.DecimalField(max_digits=8, decimal_places=1, blank=True)
    
