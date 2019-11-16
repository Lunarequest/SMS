from django.shortcuts import render
from django.http import HttpResponse
from .models import chem

# Create your views here.
def console(request):
    if(request.user.has_perm('bio.can_view_chem')):
        response = render(request,'console.html')
        return response
        
        
def edit(request):       
    if(request.user.has_perm('bio.can_change_chem') and request.user.has_perm('bio.can_add_chem') and request.user.has_perm('bio.can_delete_chem')):
        if (request.method == 'POST'):
             entries = chem.objects.all()
             context = {'entries':entries}
            #if request.user.has_perm() to check if user has permissions 
             return HttpResponse("loads")