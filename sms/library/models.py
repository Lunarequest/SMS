from django.db import models

# Create your models here.
class book_copy(models.Model):
    book_name = models.CharField(max_length=500)
    num_copy = models.PositiveIntegerField()
    num_copies_available = models.PositiveIntegerField(default=1)
class book(models.Model):
    book_id = models.PositiveIntegerField(primary_key=True)
    book_name = models.CharField(max_length=500)
    availabity = models.BooleanField(default=True)
class issues(models.Model):
    book_id = models.CharField(max_length=1000, primary_key=True)
    student_id = models.PositiveIntegerField()
    issue_date = models.DateField()
    return_date = models.DateField()
class mass_book(models.Model):
    ISBN = models.PositiveIntegerField()
    ind_book_id = models.CharField(primary_key=True, max_length=1000)

class num_ent(models.Model):
    ISBN = models.PositiveIntegerField(primary_key=True)
    num = models.PositiveIntegerField(default=0)
    
