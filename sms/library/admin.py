from django.contrib import admin
from .models import book, book_copy, issues, mass_book
# Register your models here.
admin.site.register(book)
admin.site.register(book_copy)
admin.site.register(issues)
admin.site.register(mass_book)
