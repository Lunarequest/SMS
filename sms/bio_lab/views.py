from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import bio_eq, bio_broken_eq
from django.db import connection
# Create your views here.
def ValuesQuerySetToDict(vqs):
    return [item for item in vqs]

def console(request):
    if request.user.groups.filter(name__in=['bio_member']):
        items = bio_eq.objects.all()
        loc = 'biology lab'
        return render(request,'bio_lab/console.html',locals())
    else:
        messages.info(request, "error 401 access denied")
        return redirect("/sel")
def edit(request, bio_eq_id = None):
    #item = get_object_or_404(bio_eq,pk=bio_eq_id)
    if request.user.groups.filter(name__in=['bio_member']):
        if(request.method == "POST"):
            amount = int(request.POST['amount'])
            costs = int(request.POST['costs'])
            print(costs)
            if(amount > 0):
                bio_eq.objects.filter(bio_eq_id=bio_eq_id).update(bio_eq_amount=amount)
            if(costs > 0):
                bio_eq.objects.filter(bio_eq_id=bio_eq_id).update(bio_eq_cost=costs)
            
            return redirect("/bio")
        else:
            cursor = connection.cursor()
            cursor.execute('''SELECT bio_eq_name from bio_lab_bio_eq where bio_eq_id=bio_eq_id''')
            row = cursor.fetchone()
            name = str(row[0])
            return render(request,'bio_lab/edit_item.html', locals())
#this was all me
def broken(request, bio_eq_id= None):       
    if request.user.groups.filter(name__in=['bio_member']):
        if(request.method == "POST"):
             broken=request.POST['broken']
             if (broken == "broken"):
                 cursor = connection.cursor()
                 cursor.execute('''SELECT bio_eq_amount from bio_lab_bio_eq where bio_eq_id=bio_eq_id''')
                 #data = bio_eq.objects.raw('SELECT bio_eq_amount from bio_lab_bio_eq where bio_eq_id=bio_eq_id')
                 row = cursor.fetchone()
                 amount = int(row[0])
                 amount = amount -1
                 cursor.execute('''SELECT bio_eq_name from bio_lab_bio_eq where bio_eq_id=bio_eq_id''')
                 row = cursor.fetchone()
                 name = str(row[0])
                 student_id=request.POST['student_id']
                 p = bio_broken_eq(bio_eq_id = bio_eq_id,student_id = student_id, bio_eq_name = name)
                 p.save()
                 bio_eq.objects.filter(pk=bio_eq_id).update(bio_eq_amount=amount)
                 #bio_broken_eq.object.create(bio_eq_id=bio_eq_id,student=student_id,bio_eq_name=name)

             return redirect("/bio")
        else:
            cursor = connection.cursor()
            cursor.execute('''SELECT bio_eq_name from bio_lab_bio_eq where bio_eq_id=bio_eq_id''')
            row = cursor.fetchone()
            name = str(row[0])
            return render(request,'bio_lab/delete.html', locals())
       
       
def display(request):
    items = bio_eq.objects.all()
    context ={
        'items':items
    }
    return render(request,'bio_lab/edit.html',context)
    


def save(request):
    return redirect("/bio")

def delete(request, bio_eq_id):
    bio_eq.objects.filter(pk=bio_eq_id).delete()
    return redirect("/bio")