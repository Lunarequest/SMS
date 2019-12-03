from django.shortcuts import render
from .models import book, issues
# Create your views here.
def console(request):
    items = book.objects.all()
    items2 = issues.objects.all()
    return render(request, 'library/console.html', locals())