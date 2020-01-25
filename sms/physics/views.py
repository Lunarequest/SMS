from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import phy_eq, phy_broken_eq
from django.db import connection
# Create your views here.


''''def console(request):
    if request.user.groups.filter(name__in=['phy_member']):
        items =phy_eq.objects.all()
        loc = 'physics lab'
        return render(request,'physicis/console.html',locals())
    else:
        messages.info(request, "error 401 access denied")
        return redirect("/sel")'''

def edit(request, phy_eq_id = None):
    #item = get_object_or_404(bio_eq,pk=bio_eq_id)
    if request.user.groups.filter(name__in=['phy_member']):
        if(request.method == "POST"):
            amount = int(request.POST['amount'])
            costs = int(request.POST['costs'])
            print(costs)
            if(amount > 0):
                phy_eq.objects.filter(phy_eq_id=phy_eq_id).update(phy_eq_amount=amount)
            if(costs > 0):
                phy_eq.objects.filter(phy_eq_id=phy_eq_id).update(phy_eq_cost=costs)

            return redirect("/physics")
        else:
            cursor = connection.cursor()
            cursor.execute('''SELECT phy_eq_name from physics_phy_eq where phy_eq_id=phy_eq_id''')
            row = cursor.fetchone()
            name = str(row[0])
            return render(request,'physicis/edit_item.html', locals())
#this was all me
def broken(request, phy_eq_id = None):
    if request.user.groups.filter(name__in=['phy_member']):
        if(request.method == "POST"):
             broken=request.POST['broken']
             if (broken == "broken"):
                 cursor = connection.cursor()
                 cursor.execute('''SELECT phy_eq_amount from physics_phy_eq where phy_eq_id=phy_eq_id''')
                 #data = bio_eq.objects.raw('SELECT bio_eq_amount from bio_lab_bio_eq where bio_eq_id=bio_eq_id')
                 row = cursor.fetchone()
                 amount = int(row[0])
                 amount = amount -1
                 cursor.execute('''SELECT phy_eq_name from physics_phy_eq where phy_eq_id=phy_eq_id''')
                 row = cursor.fetchone()
                 name = str(row[0])
                 student_id=request.POST['student_id']
                 p = phy_broken_eq(phy_eq_id = bio_eq_id,student_id = student_id, bio_eq_name = name)
                 p.save()
                 phy_eq.objects.filter(pk=phy_eq_id).update(phy_eq_amount=amount)
                 #bio_broken_eq.object.create(bio_eq_id=bio_eq_id,student=student_id,bio_eq_name=name)

             return redirect("/physics")
        else:
            cursor = connection.cursor()
            cursor.execute('''SELECT bio_eq_name from bio_lab_bio_eq where bio_eq_id=bio_eq_id''')
            row = cursor.fetchone()
            name = str(row[0])
            return render(request,'physicis/delete.html', locals())


def display(request):
    items = phy_eq.objects.filter(safety=True)
    items2 = phy_eq.objects.filter(safety=False)
    loc = "Phyisics"
    context ={
        'items':items,
        'items2':items2,
        'loc':loc
    }
    return render(request,'physicis/edit.html',context)



def save(request):
    return redirect("/physics")

def delete(request, phy_eq_id):
    phy_eq.objects.filter(pk=phy_eq_id).delete()
    return redirect("/physics")

def add(request):
    if request.user.groups.filter(name__in=['phy_member']):
        if(request.method=="POST"):
            phy_eq_id = request.POST['id']
            phy_eq_name = request.POST['name']
            phy_eq_amount = int(request.POST['amount'])
            phy_eq_cost = int(request.POST['cost'])
            safety = request.POST['safety']
            if phy_eq.objects.filter(phy_eq_id=phy_eq_id).exists():
                message = messages.info(request,"equipment id is not unique")
                return redirect("/phy/add")
            elif(phy_eq_amount<=0):
                message = messages.info(request,"invalid ammount")
                return redirect("/phy/add")
            else:
                p = phy_eq(phy_eq_id=phy_eq_id,phy_eq_name=phy_eq_name, phy_eq_amount=phy_eq_amount, phy_eq_cost=phy_eq_cost, safety=safety)
                p.save()
                return redirect("/phy")
        else:
            return render(request,'physicis/add.html', locals())
