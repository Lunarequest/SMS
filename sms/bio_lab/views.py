from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import bio_eq
# Create your views here.


def console(request):
    if request.user.groups.filter(name__in=['bio_member']):
        istekler = bio_eq.objects.all()
        loc = 'biology lab'
        return render(request,'bio_lab/console.html',locals())
    else:
        messages.info(request, "error 401 access denied")
        return redirect("/sel")

def edit(request):       
    if request.user.groups.filter(name__in=['bio_member']):
        table = bio_eq.objects.all()
        loc = 'biology lab'
        return render(request,"bio_lab/edit.html",locals())