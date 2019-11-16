from django.shortcuts import render
from django.http import HttpResponse
from .models import chem

# Create your views here.
def console(request):
    if(request.user.has_perm():
        if (request.method == 'POST'):
            entries = chem.objects.all()
            context = {'entries':entries}
            #if request.user.has_perm() to check if user has permissions 
            return HttpResponse("loads")
            
        else:
            response = HttpResponse('works')
            response = render(request,'console.html')
            return response