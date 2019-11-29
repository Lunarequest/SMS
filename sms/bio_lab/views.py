from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import bio_eq
# Create your views here.


def console(request):
    if request.user.groups.filter(name__in=['bio_member']):
        items = bio_eq.objects.all()
        loc = 'biology lab'
        return render(request,'bio_lab/console.html',locals())
    else:
        messages.info(request, "error 401 access denied")
        return redirect("/sel")

def edit(request, pk):       
    if request.user.groups.filter(name__in=['bio_member']):
        item = get_object_or_404(bio_eq,pk=pk)
        if(request.method == "POST"):
            form = bio_equipmentform(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect("/bio")
        else:
            form = bio_equipmentform(instance=item)
            return render(request,'edit_equipmet.html', {form:form})
       
       
       
       
        """table = bio_eq.objects.all()
        loc = 'biology lab'
        return render(request,"bio_lab/edit.html",locals())"""


def save(request):
    return redirect("/bio")