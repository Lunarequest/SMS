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
def edit(request):
    if request.user.groups.filter(name__in=['chem_member']):
        items = chem_con.objects.all()
        loc = 'chemistry lab'
        items2=chem_eq.objects.all()
        return render(request,'chem_lab/edit.html',locals())
def edit_con(request, consumable_id):
     if request.user.groups.filter(name__in=['chem_member']):
        if(request.method == "POST"):
             amount=int(request.POST['amount'])
             date=request.POST['exp_date']
             chem_con.objects.filter(consumable_id=consumable_id).update(chem_amount=amount)
             chem_con.objects.filter(consumable_id=consumable_id).update(exp_date=date)
             return redirect("/physics")
        else:
            return render(request,'chem_lab/edit_con_item.html')

def broken(request, chem_eq_id):
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

def edit_eq(request, chem_eq_id):
    if request.user.groups.filter(name__in=['chem_member']):
        if(request.method=="POST"):
            amount=int(request.POST['amount'])
            cost=int(request.POST['costs'])
            if(amount>0):
                chem_eq.objects.filter(chem_eq_id=chem_eq_id).update(chem_eq_amount=amount)
            if(cost>0):
                chem_eq.objects.filter(chem_eq_id=chem_eq_id).update(chem_eq_cost=cost)
            return redirect("/chem")
        else:
            cursor = connection.cursor()
            cursor.execute('''SELECT chem_names from chem_lab_chem_con where consumable_id=consumable_id''')
            row=cursor.fetchone()
            chem = row[0]
            return render(request,'chem_lab/edit_eq.html', locals())
def add_con(request):
    if request.user.groups.filter(name__in=['chem_member']):
        if(request.method=="POST"):
            con_id = request.POST['id']
            name = request.POST['chem_name']
            amount = request.POST['q']
            exp_date = request.POST['exp_date']
            if(chem_con.objects.filter(consumable_id=con_id).exists()):
                messages.info(request,'consumable id is not uniqe!')
                return redirect("/chem/add_con")
            else:
                q=chem_con(consumable_id=con_id, chem_names=name,  chem_amount=amount, exp_date=exp_date)
                q.save()
        else:

            return render(request,'chem_lab/add_con.html')
def add_eq(request):
      if request.user.groups.filter(name__in=['chem_member']):
        if(request.method=="POST"):
            con_id = request.POST['id']
            name = request.POST['eq_name']
            amount = request.POST['q']
            cost = request.POST['costs']
            if(chem_eq.objects.filter(chem_eq_id=con_id).exists()):
                messages.info(request,'equipment id is not uniqe!')
                return redirect("/chem/add_eq")
            else:
                q=chem_eq(chem_eq_id=con_id, chem_eq_names=name,  chem_eq_amount=amount, chem_eq_cost=cost)
                q.save()
                return redirect("/chem")
        else:
            return render(request,'chem_lab/add_eq.html')
