from django.db import models

# Create your models here.
class phy_broken_eq(models.Model):
  phy_eq_id = models.IntegerField(primary_key = True)
  student_id = models.PositiveIntegerField()
  phy_eq_name = models.CharField(max_length=50)
  

class phy_eq(models.Model):
  phy_eq_id = models.IntegerField(primary_key=True)
  phy_eq_name = models.CharField(max_length=50)
  phy_eq_amount = models.PositiveIntegerField()
  phy_eq_cost = models.IntegerField()
  safety = models.BooleanField(default=False)