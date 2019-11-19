from django.shortcuts import render
from django.http import HttpResponse
from .models import chem

# Create your views here.


def console(request):
    if request.user.groups.filter(name__in=['bio_member']):
        istekler = chem.objects.all()
        return render(request,'console.html',locals())


def edit(request):       
    if request.user.qroups.filter(name_in=['bio_member']):
        if (request.method == 'POST'):
             entries = chem.objects.all()
            #MyModel.objects.filter(pk=some_value).update(field1='some value')
             return HttpResponse("loads")