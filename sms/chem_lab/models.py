from django.db import models

# Create your models here.

class chem_con(models.Model):
    consumable_id = models.IntegerField(primary_key=True)
    chem_names = models.CharField(max_length=50)
    chem_amount = models.FloatField()
    exp_date = models.CharField(max_length=50)
    reo = models.PositiveIntegerField()

class chem_eq(models.Model):
    chem_eq_id = models.IntegerField(primary_key=True)
    chem_eq_names = models.CharField(max_length=50)
    chem_eq_amount = models.PositiveIntegerField()
    chem_eq_cost  = models.PositiveIntegerField()
class ch_broken_eq(models.Model):
    chem_eq_id = models.IntegerField(primary_key=True)
    student = models.PositiveIntegerField()
    chem_eq_names = models.CharField(max_length=50)
    #chem_eq_number = models.PositiveIntegerField()
    
