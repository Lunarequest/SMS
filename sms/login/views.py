from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth, User

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/sel")
        else:
            messages.info(request,'invaild login')
            return redirect("/login")
    else:
        return render(request,'login_new.html')

def logout(request):
    auth.logout(request)
    return redirect("login")