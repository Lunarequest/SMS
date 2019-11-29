from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import chem_con, chem_eq, ch_broken_eq

# Create your views here.


def console(request):
    if request.user.groups.filter(name__in=['chem_member']):
        istekler = chem.objects.all()
        loc = 'chemistry lab'
        return render(request,'console.html',locals())
    else:
        messages.info(request, "error 401 access denied")
        return redirect("/sel")

def edit_con(request,bio_eq_id):       
     if request.user.groups.filter(name__in=['chem_member']):
        item = get_object_or_404(chem_con,pk=bio_eq_id)
        if(request.method == "POST"):
             amount=request.POST['amount']
             if (broken == "broken"):
                 item = chem_con.objects.filter(pk=bio_eq_id)
                 amount = item.amount-amount
                 chem_con.objects.filter(pk=bio_eq_id).update(amount=amount)

             return redirect("/physics")
        else:
            return render(request,'chem/edit_con_item.html')
       
def broken(request, bio_eq_id):
     if request.user.groups.filter(name__in=['chem_member']):
        item = get_object_or_404(chem_eq,pk=bio_eq_id)
        if(request.method == "POST"):
             broken=request.POST['broken']
             student_id=request.POST['student_id']
             if (broken == "broken"):
                 item = chem_eq.objects.filter(pk=bio_eq_id)
                 amount=item.amount
                 name = item.chem_eq_name
                 chem_eq.objects.filter(pk=bio_eq_id).update(amount=amount-1)
                 ch_broken_eq.object.create(chem_eq_id=bio_eq_id,student=student_id,chem_eq_name=name)

             return redirect("/chem")
        else:
            return render(request,'chem_lab/broken_item.html')
       

