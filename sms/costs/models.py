from django.db import models

# Create your models here.

class student(models.Model):
    student_id = models.PositiveIntegerField(primary_key=True)
    student_name = models.CharField(max_length=50)
    student_grade = models.IntegerField()
    student_section = models.CharField(max_length=500)

class grade(models.Model):
    student_grade = models.PositiveIntegerField()
    student_section = models.CharField(max_length=500)
    teacher_email_1 = models.EmailField()
    teacher_email_2 = models.EmailField()

class super_email(models.Model):
    supervisor_email = models.EmailField()