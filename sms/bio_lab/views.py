from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import chem

# Create your views here.


def console(request):
    if request.user.groups.filter(name__in=['bio_member']):
        istekler = chem.objects.all()
        loc = 'biology lab'
        return render(request,'bio_lab/console.html',locals())
    else:
        messages.info(request, "error 401 access denied")
        return redirect("/sel")

def edit(request):       
    if request.user.qroups.filter(name_in=['bio_member']):
        if (request.method == 'POST'):
             entries = chem.objects.all()
            #MyModel.objects.filter(pk=some_value).update(field1='some value')
             return HttpResponse("loads")
        else:
            return render(request,"bio_lab/edit.html")