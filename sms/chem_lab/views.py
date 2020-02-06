from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import chem_con, chem_eq, ch_broken_eq
from costs.models import  super_email
from django.db import connection
# Create your views here.


"""def console(request):
    if request.user.groups.filter(name__in=['chem_member']):
        items = chem_con.objects.all()
        loc = 'chemistry lab'
        items2=chem_eq.objects.filter()
        return render(request,'chem_lab/console.html',locals())
    else:
        messages.info(request, "error 401 access denied")
        return redirect("/sel")"""
def edit(request):
    if request.user.groups.filter(name__in=['chem_member']):
        loc = "Chemistry"
        items = chem_con.objects.filter(aqua=True)
        items1 = chem_con.objects.filter(aqua=False)
        items2 = chem_eq.objects.filter(safety=True)
        items3 = chem_eq.objects.filter(safety=False)
        return render(request,'chem_lab/edit.html',locals())
    else:
        messages.info(request, "error 401 access denied")
        return redirect("/sel")
def edit_con(request, consumable_id):
     if request.user.groups.filter(name__in=['chem_member']):
        if(request.method == "POST"):
             amount=int(request.POST['amount'])
             date=request.POST['exp_date']
             chem_con.objects.filter(consumable_id=consumable_id).update(chem_amount=amount)
             chem_con.objects.filter(consumable_id=consumable_id).update(exp_date=date)
             cursor = connection.cursor()
             cursor.execute('''SELECT reo FROM chem_lab_chem_con WHERE consumable_id=consumable_id''')
             temp = cursor.fetchone()
             reo = int(temp[0])
             return redirect("/chem")
             if(amount<=reo):
                cursor.execute('''SELECT chem_names FROM chem_lab_chem_con WHERE consumable_id=consumable_id''')
                temp = cursor.fetchone()
                chem_name = temp[0]
                email_subject = "reorder " + chem_name
                message = "please reorder " + chem_name
                temp = super_email.objects.values("supervisor_email").filter('*').values_list('supervisor_email ')
                to_email = temp[0]
                msg = str(student_name + " has not returend " + book_name + "please ensure it is returned")
                send_mail(
                'late dues',
                msg,
                'localhost',
                [to_email],
                fail_silently=False,
            )
                
        else:
            name =chem_con.objects.values('chem_names').filter(consumable_id=consumable_id).values_list('chem_names', flat=True)
            name = name[0]
            return render(request,'chem_lab/edit_con_item.html', locals())

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
                 p=ch_broken_eq(chem_eq_id=chem_eq_id, student_id=student_id, chem_eq_name=name)
                 p.save()
                 chem_eq.objects.filter(chem_eq_id=chem_eq_id).update(chem_eq_amount=amount)
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
            name = chem_eq.objects.values('chem_eq_names').filter(chem_eq_id=chem_eq_id).values_list('chem_eq_names', flat=True)
            name = name[0]
            return render(request,'chem_lab/edit_eq.html', locals())
def add_con(request):
    if request.user.groups.filter(name__in=['chem_member']):
        if(request.method=="POST"):
            con_id = request.POST['id']
            name = request.POST['chem_name']
            amount = request.POST['q']
            reo = request.POST['reo']
            exp_date = request.POST['exp_date']
            aqua = request.POST['Type']
            if(chem_con.objects.filter(consumable_id=con_id).exists()):
                messages.info(request,'consumable id is not uniqe!')
                return redirect("/chem/add_con")
            else:
                q=chem_con(consumable_id=con_id, chem_names=name,  chem_amount=amount, exp_date=exp_date, reo=reo, aqua=aqua)
                q.save()
                return redirect("/chem")
        else:
            return render(request,'chem_lab/add_con.html')
def add_eq(request):
      if request.user.groups.filter(name__in=['chem_member']):
        if(request.method=="POST"):
            con_id = request.POST['id']
            name = request.POST['eq_name']
            amount = request.POST['q']
            cost = request.POST['costs']
            safety = request.POST['Safety']
            if(chem_eq.objects.filter(chem_eq_id=con_id).exists()):
                messages.info(request,'equipment id is not uniqe!')
                return redirect("/chem/add_eq")
            else:
                q=chem_eq(chem_eq_id=con_id, chem_eq_names=name,  chem_eq_amount=amount, chem_eq_cost=cost, safety=safety)
                q.save()
                return redirect("/chem")
        else:
            return render(request,'chem_lab/add_eq.html')
