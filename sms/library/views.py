"""for date"""
import datetime
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.core.mail import EmailMessage
from costs.models import student
from costs.models import grade as grades
from .models import book, issues, book_copy, mass_book, num_ent
from django.core.mail import send_mail
# Create your views here
#ported
def console(request):
    '''to display the website when requested'''
    if request.user.groups.filter(name__in=['lib_member']):
        if(request.method == "POST"):
            q = request.POST['q']
            search = mass_book.objects.filter(ISBN=q)
            return render(request, "library/console.html", locals())
        else:
            items = book.objects.all()
            item3 = issues.objects.all()
            item2 = mass_book.objects.filter(issued=False)
            late_books = issues.objects.filter(return_date__lt=datetime.date.today())
            return render(request, 'library/console.html', locals())
    else:
        message = messages.info(request, 'error 401 access denied')
        return redirect("/sel")
#ported
def report(request, book_id):
    book_name = issues.objects.values('book_name').filter(book_id=book_id).values_list('book_name', flat=True)
    book_name = book_name[0]
    student_id = issues.objects.values('student_id').filter(book_id=book_id).values_list('student_id', flat=True)
    student_id = int(student_id[0])
    student_name = student.objects.values('student_name').filter(student_id=student_id).values_list('student_name', flat=True)
    student_name = str(student_name[0])
    grade = student.objects.values('student_grade').filter(student_id=student_id).values_list('student_grade', flat=True)
    grade = int(grade[0])
    section = student.objects.values('student_section').filter(student_id=student_id).values_list('student_section', flat=True)
    section = str(section[0])
    email1 = grades.objects.values('teacher_email_1').filter(student_grade=grade).filter(student_section=section).values_list('teacher_email_1', flat=True)
    email1 = str(email1[0])
    email2 = grades.objects.values('teacher_email_2').filter(student_grade=grade).filter(student_section=section).values_list('teacher_email_2', flat=True)
    email2 = str(email2[0])
    msg = str(student_name + " has not returend " + book_name + "please ensure it is returned")
    send_mail(
        'late dues',
        msg,
        'localhost',
        [email1,email2],
        fail_silently=False,
    )
    return redirect('/library')
    
#ported
def issue(request, ind_book_id):
    '''issues one book'''
    if request.user.groups.filter(name__in=['lib_member']):
        if(request.method == "POST"):
            student_id = request.POST.get('student_id')
            return_date = request.POST.get('rt_date')
            if(student.objects.filter(student_id=student_id).exists()):
                cursor = connection.cursor()
                date = datetime.date.today()
                book_id = mass_book.objects.values('ISBN').filter(ind_book_id=ind_book_id).values_list('ISBN', flat=True)
                book_id = int(book_id[0])
                book_name = book.objects.values('book_name').filter(book_id=book_id).values_list('book_name', flat=True)
                book_name = book_name[0]
                avil = book_copy.objects.filter(book_name=book_name).values_list('num_copy', flat=True)
                avil = int(avil[0]) -1
                p = issues(ISBN=book_id, book_id=ind_book_id, student_id=student_id, book_name=book_name, issue_date=date, return_date=return_date)
                book_copy.objects.filter(book_name=book_name).update(num_copies_available = avil)
                mass_book.objects.filter(ind_book_id=ind_book_id).update(issued=True)
                p.save()
                
                return redirect("/library")
        else:
            book_id = mass_book.objects.values('ISBN').filter(ind_book_id=ind_book_id).values_list('ISBN', flat=True)
            book_id = int(book_id[0])
            book_name = book.objects.values('book_name').filter(book_id=book_id).values_list('book_name', flat=True)
            name = book_name[0]
            return render(request, 'library/issue.html', locals())

#ported
def add(request):
    '''adds books from request'''
    if request.user.groups.filter(name__in=['lib_member']):
        if(request.method == "POST"):
            book_id = request.POST['book_id']
            if book_id:
                book_name = request.POST['book_name']
                if book_name:
                    num_copy = request.POST['num_copy']
                    if num_copy:
                        num_copy=int(num_copy)
                        if(book.objects.filter(book_id=book_id).exists()):
                            messagez = messages.info(request, "book id exits")
                            return redirect("library/add")
                        elif(num_copy <= 0):
                            messagez = messages.info(request, "enter valid amount of books")
                            return redirect("library/add")
                        else:
                            p = book_copy(book_name=book_name, num_copy=num_copy, num_copies_available=num_copy )
                            p.save()
                            q = book(book_id=book_id, book_name=book_name,  availabity=True)
                            q.save()
                            w = num_ent(ISBN=book_id, num=0)
                            return redirect("/library")
                    else:
                        messagez = messages.info(request, "Invalid input")
                        return redirect("/library/add")
                else:
                    messagez = messages.info(request, "Invalid input")
                    return redirect("/library/add")
            else:
                messagez = messages.info(request, "Invalid input")
                return redirect("/library/add")
        else:
            return render(request, 'library/add.html')
#ported 
def add_copy_id(request, book_id):
    if request.user.groups.filter(name__in=['lib_member']):
        if(request.method == "POST"):
            book_name = book.objects.values('book_name').filter(book_id=book_id).values_list('book_name', flat=True)
            book_name = book_name[0]
            ind_book_id = request.POST['book_id']
            if mass_book.objects.filter(ind_book_id=ind_book_id).exists():
                message = messages.info(request, "id already exists")
                return render(request, 'library/add_copy_id.html', locals())
            else:
                issued = False
                q = mass_book(ISBN=book_id, ind_book_id=ind_book_id, book_name=book_name, issued=issued)
                q.save()
                return redirect("/library")
        else:
            book_name = book.objects.values('book_name').filter(book_id=book_id).values_list('book_name', flat=True)
            books = str(book_name[0])
            return render(request, 'library/add_copy_id.html',locals())
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
        ind_book_id = book_id
        print(ind_book_id)
        issued = True
        if mass_book.objects.filter(pk=ind_book_id):
            mass_book.objects.filter(ind_book_id=ind_book_id).update(issued=False)
        else:
            print('fail')
        return redirect("/library")
