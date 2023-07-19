from django.db import models

# Create your models here.

class Index(models.Model):
    ins_code = models.CharField(max_length=20, unique=True)
    lval30 = models.CharField(max_length=40)

class IndexHistory(models.Model):
    index = models.ForeignKey(Index, related_name='histories', on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True)
    low = models.DecimalField(max_digits=8, decimal_places=1, blank=True)
    high = models.DecimalField(max_digits=8, decimal_places=1, blank=True)
    close = models.DecimalField(max_digits=8, decimal_places=1, blank=True)
    
