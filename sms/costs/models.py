from django.db import models

# Create your models here.

class student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=50)
    student_grade = models.IntegerField()