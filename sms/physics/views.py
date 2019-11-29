from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import bio_eq
# Create your views here.


def console(request):
    if request.user.groups.filter(name__in=['bio_member']):
        items = bio_eq.objects.all()
        loc = 'biology lab'
        return render(request,'bio_lab/edit.html',locals())
    else:
        messages.info(request, "error 401 access denied")
        return redirect("/sel")

def edit(request, bio_eq_id= None):       
    if request.user.groups.filter(name__in=['bio_member']):
        item = get_object_or_404(bio_eq,pk=bio_eq_id)
        if(request.method == "POST"):
             broken=request.POST['broken']
             if (broken == "broken"):
                 item = bio_eq.objects.filter(pk=bio_eq_id)
                 amount=item.amount
                 bio_eq.objects.filter(pk=bio_eq_id).update(amount=amount-1)

             return redirect("/bio")
        else:
            return render(request,'bio_lab/edit_item.html')
       
       
       
    


def save(request):
    return redirect("/bio")