from django.contrib import admin
from .models import student, grade, super_email
# Register your models here.
admin.site.register(student)
admin.site.register(grade)
admin.site.register(super_email)