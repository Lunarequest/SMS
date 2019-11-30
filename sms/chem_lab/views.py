from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import chem_con, chem_eq, ch_broken_eq
from django.db import connection
# Create your views here.


def console(request):
    if request.user.groups.filter(name__in=['chem_member']):
        items = chem_con.objects.all()
        loc = 'chemistry lab'
        items2=chem_eq.objects.all()
        return render(request,'chem_lab/console.html',locals())
    else:
        messages.info(request, "error 401 access denied")
        return redirect("/sel")

def edit_con(request,bio_eq_id):       
     if request.user.groups.filter(name__in=['chem_member']):
        if(request.method == "POST"):
             amount=request.POST['amount']
             date=request.POST['exp_date']
             chem_con.objects.filter(consumable_id=bio_eq_id).update(chem_amount=amount)
             chem_con.objects.filter(consumable_id=bio_eq_id).update(exp_date=date)
             return redirect("/physics")
        else:
            return render(request,'chem/edit_con_item.html')
       
def broken(request, bio_eq_id):
     if request.user.groups.filter(name__in=['chem_member']):
        if(request.method == "POST"):
             broken=request.POST['broken']
             student_id=request.POST['student_id']
             if (broken == "broken"):
                 cursor = connection.cursor()
                 cursor.execute('''SELECT chem_eq_amount from chem_lab_chem_eq where chem_eq_id=bio_eq_id''')
                 row=cursor.fetchone()
                 amount=int(row[0])
                 amount=amount-1
                 cursor.execute('''SELECT chem_eq_name from chem_lab_chem_eq where chem_eq_id=bio_eq_id''')
                 row=cursor.fetchone()
                 name=str(row[0])
                 p=ch_broken_eq(chem_eq_id=bio_eq_id, student_id=student_id, chem_eq_name=name)
                 p.save()
                 chem_eq.objects.filter(chem_eq_id=bio_eq_id).update(chem_eq_amount=amount)
                 return redirect("/chem")
        else:
            return render(request,'chem_lab/broken_item.html')
       

