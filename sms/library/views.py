"""for date"""
import datetime
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from costs.models import student
from .models import book, issues, book_copy, mass_book, num_ent
# Create your views here
def console(request):
    '''to display the website when requested'''
    if request.user.groups.filter(name__in=['lib_member']):
        cursor = connection.cursor()
        items = book.objects.all()
        item3 = issues.objects.all()
        today = datetime.date.today()
        item2 = mass_book.objects.all()
        late_books = issues.objects.filter(return_date__lte=today)
        return render(request, 'library/console.html', locals())
    else:
        message = messages.info(request, 'error 401 access denied')
        return redirect("/sel")


def issue(request, ind_book_id):
    '''issues one book'''
    if request.user.groups.filter(name__in=['lib_member']):
        if(request.method == "POST"):
            student_id = request.POST.get('student_id')
            return_date = request.POST.get('rt_date')
            if(student.objects.filter(student_id=student_id).exists()):
                cursor = connection.cursor()
                date = datetime.date.today()
                cursor.execute('''SELECT ISBN FROM library_mass_book WHERE ind_book_id=ind_book_id''')
                row = cursor.fetchone()
                book_id = row[0]
                p = issues(book_id=ind_book_id, student_id=student_id, issue_date=date, return_date=return_date)
                p.save()
                cursor.execute('''SELECT book_name FROM library_book WHERE book_id=book_id''')
                x=cursor.fetchone()
                book_name = x[0]
                cursor.execute('''SELECT num_copies_available FROM library_book_copy WHERE book_name=book_name''')
                x= cursor.fetchone()
                avil = x[0]
                avil = avil-1
                book_copy.objects.filter(book_name=book_name).update(num_copies_available = avil)
                if(avil == 0):
                    book.objects.filter(book_id=book_id).update(avilabilty=False)
                return redirect("/library")
        else:
            cursor = connection.cursor()
            cursor.execute('''SELECT book_name FROM library_book WHERE book_id=book_id''')
            name = str(cursor.fetchone())
            return render(request, 'library/issue.html', locals())


def add(request):
    '''adds books from request'''
    if request.user.groups.filter(name__in=['lib_member']):
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
                p = book_copy(book_name=book_name, num_copy=num_copy, num_copies_available=num_copy )
                p.save()
                q = book(book_id=book_id, book_name=book_name,  availabity=True)
                q.save()
                return redirect("/library")
        else:
            return render(request, 'library/add.html')
def add_copy_id(request, book_id):
    from django.contrib import messages
    if request.user.groups.filter(name__in=['lib_member']):
        if(request.method == "POST"):
            cursor = connection.cursor()
            ISBN = book_id
            cursor.execute('''SELECT num FROM library_num_ent WHERE ISBN=ISBN''')
            x = cursor.fetchone()
            number = int(x[0])
            cursor.execute('''SELECT book_name FROM library_book WHERE book_id=book_id''')
            x = cursor.fetchone()
            book_name = x[0]
            book_name = str(book_name)
            cursor.execute('''SELECT num_copies_available FROM library_book_copy WHERE book_name=book_name''')
            x = cursor.fetchone()
            num_copy = int(x[0])
            if(number != num_copy):
                if(request.method == "POST"):
                    ind_book_id = request.POST['book_id']
                    if mass_book.objects.filter(ind_book_id=ind_book_id).exits():
                        message = messages.info(request, "id already exists")
                        return redirect("/library")
                    else:
                        q = mass_book(ISBN=book_id, ind_book_id=ind_book_id)
                        q.save()
                        number = number + 1
                        num_ent.objects.filter(ISBN=ISBN).update(num=number)
                        return redirect("/library")
        else:
            return render(request, 'library/add_copy_id.html')
    else:
        message = messages.info(request,"error 401 acesss denid")
        return redirect("/library", locals())    
def delete(request, ind_book_id):
    """removes a book permenatly"""
    if request.user.groups.filter(name__in=['lib_member']):
        cursor = connection.cursor()
        cursor.execute('''SELECT ISBN FROM library_mass_book WHERE ind_book_id=ind_book_id''')
        temp = cursor.fetchone()
        book_id = int(temp[0])
        cursor.execute('''SELECT book_name FROM library_book WHERE book_id = book_id''')
        book_name = cursor.fetchone()
        cursor.execute('''SELECT num_copy FROM library_book_copy WHERE book_name=book_name''')
        x = cursor.fetchone()
        num = int(x[0])
        num = num - 1
        book_copy.objects.filter(book_name=book_name).update(num_copy=num)
        mass_book.objects.filter(ind_book_id=ind_book_id).delete()
        return redirect("/library")

def return_book(request, book_id):
    """returns an issued book"""
    if request.user.groups.filter(name__in=['lib_member']):
        issues.objects.filter(pk=book_id).delete()
        cursor = connection.cursor()
        cursor.execute('''SELECT book_name FROM library_book WHERE book_id=book_id''')
        row = cursor.fetchone()
        book_name = row[0]
        cursor.execute('''SELECT num_copies_available FROM library_book_copy WHERE book_name=book_name''')
        row = cursor.fetchone()
        avil = row[0]
        avil = avil + 1
        book_copy.objects.filter(book_name=book_name).update(num_copies_available=avil)
        return redirect("/library")
