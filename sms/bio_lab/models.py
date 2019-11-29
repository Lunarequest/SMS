from django.db import models
#from chem_lab.models import student
# Create your models here.
class bio_broken_eq(models.Model):
  bio_eq_id = models.IntegerField(primary_key = True)
  student_id = models.PositiveIntegerField()
  bio_eq_name = models.CharField(max_length=50)
  

class bio_eq(models.Model):
  bio_eq_id = models.IntegerField(primary_key=True)
  bio_eq_name = models.CharField(max_length=50)
  bio_eq_amount = models.PositiveIntegerField()
  bio_eq_cost = models.IntegerField()