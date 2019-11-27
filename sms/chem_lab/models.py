from django.db import models

# Create your models here.

class student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=50)
    student_grade = models.IntegerField()
class chem_con(models.Model):
    consumable_id = models.IntegerField(primary_key=True)
    chem_names = models.CharField(max_length=50)
    chem_amount = models.PositiveIntegerField()
    exp_date = models.CharField(max_length=50)

class chem_eq(models.Model):
    chem_eq_id = models.IntegerField(primary_key=True)
    chem_eq_names = models.CharField(max_length=50)
    chem_eq_amount = models.PositiveIntegerField()

class ch_broken_eq(models.Model):
    chem_eq_id = models.IntegerField(primary_key=True)
    student = models.ForeignKey("chem_lab.student", verbose_name=("student"), on_delete=models.CASCADE)
    chem_eq_names = models.CharField(max_length=50)
    chem_eq_number = models.PositiveIntegerField()
    chem_eq_cost  = models.PositiveIntegerField()
