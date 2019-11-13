from django.db import models

# Create your models here.
class chem(models.Model):
    serialnum = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10000)
    amount = models.IntegerField(max_length=None)
