from django.contrib import admin
from .models import student, chem_eq, chem_con, ch_broken_eq
# Register your models here.
admin.site.register(student)
admin.site.register(chem_eq)
admin.site.register(chem_con)
admin.site.register(ch_broken_eq)
