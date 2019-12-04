from django.shortcuts import render, redirect
from .models import book, issues, book_copy
from django.db import connection
from django.http import HttpResponse
from django.contrib import messages
from costs.models import student
# Create your views here.
def console(request):
    items = book.objects.all()
    items2 = issues.objects.all()
    return render(request, 'library/console.html', locals())

def issue(request, book_id):
    if(request.method == "POST"):
        student_id = request.POST['student_id']
        if(student.objects.filter(student_id=student_id).extist()):
            p = issues()
            return HttpResponse('works')
    else:
        cursor = connection.cursor()
        cursor.execute('''SELECT book_name FROM library_book WHERE book_id=book_id''')
        name = str(cursor.fetchone())
        return render(request, 'library/issue.html', locals())

def add(request):
    if(request.method == "POST"):
        book_id = request.POST['book_id']
        book_name = request.POST['book_name']
        num_copy = int(request.POST['num_copy'])
        if(book.objects.filter(book_id=book_id).exists()):
            message.info(request,"book id exits")
            return redirect("library/add")
        elif(num_copy<=0):
            messages.info(request,"enter valid amount of books")
            return redirect("library/add")
        else:
            p = book_copy(book_name = book_name, num_copy = num_copy, num_copies_available = num_copy )
            p.save()
            q = book(book_id = book_id, book_name =book_name,  availabity = True)
            q.save()
            return redirect("/library")
    else:
        return render(request, 'library/add.html')