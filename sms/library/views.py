from django.shortcuts import render, redirect
from .models import book, issues, book_copy
from django.db import connection
from django.http import HttpResponse
from django.contrib import messages
from costs.models import student
import datetime
# Create your views here
def console(request):
    cursor = connection.cursor()
    items = book.objects.all()
    items2 = book_copy.objects.all()
    item3 = issues.objects.all()
    today = datetime.date.today()
    late_books = issues.objects.filter(return_date__lte=today)
    return render(request, 'library/console.html', locals())


def issue(request, book_id):
    if(request.method == "POST"):
        student_id = request.POST.get('student_id')
        return_date = request.POST.get('rt_date')
        if(student.objects.filter(student_id=student_id).exists()):
            cursor = connection.cursor()
            date = datetime.date.today()
            p = issues(book_id=book_id, student_id=student_id, issue_date=date,return_date=return_date)
            p.save()
            cursor.execute('''SELECT book_name FROM library_book WHERE book_id=book_id''')
            x =cursor.fetchone()
            book_name = x[0]
            cursor.execute('''SELECT num_copies_available FROM library_book_copy WHERE book_name=book_name''')
            x = cursor.fetchone()
            avil = x[0]
            avil = avil-1
            book.objects.filter(book_name=book_name).update(num_copies_available = avil)
            if(avil == 0):
                book.objects.filter(book_id=book_id).update(avilabilty=False)
            return redirect("/library")
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
            messages.info(request, "book id exits")
            return redirect("library/add")
        elif(num_copy <= 0):
            messages.info(request, "enter valid amount of books")
            return redirect("library/add")
        else:
            p = book_copy(book_name = book_name, num_copy = num_copy, num_copies_available = num_copy )
            p.save()
            q = book(book_id = book_id, book_name =book_name,  availabity = True)
            q.save()
            return redirect("/library")
    else:
        return render(request, 'library/add.html')


def delete(request, book_id):
    cursor = connection.cursor()
    cursor.execute('''SELECT book_name FROM library_book WHERE book_id = book_id''')
    name = cursor.fetchone()
    book.objects.filter(pk=book_id).delete()
    book_copy.objects.filter(book_name = name).delete()
    return redirect("/library")

def return_book(request, book_id):
    issues.objects.filter(pk=book_id).delete()
    cursor = connection.cursor()
    cursor.execute('''SELECT book_name FROM library_book WHERE book_id=book_id''')
    x = cursor.fetchone()
    book_name = x[0]
    cursor.execute('''SELECT num_copies_available FROM library_book_copy WHERE book_name=book_name''')
    x = cursor.fetchone()
    avil = x[0]
    avil = avil + 1
    book_copy.objects.filter(book_name=book_name).update(num_copies_available=avil)
    return redirect("/library")