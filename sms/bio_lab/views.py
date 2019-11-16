from django.shortcuts import render
from django.http import HttpResponse
from .models import chem

# Create your views here.
def console(request):
    if(request.user.has_perm('bio.can_view_chem')):
        istekler = chem.objects.all()
        return render(request,'console.html',locals())
def edit(request):       
    if(request.user.has_perm('bio.can_change_chem') and request.user.has_perm('bio.can_add_chem') and request.user.has_perm('bio.can_delete_chem')):
        if (request.method == 'POST'):
             entries = chem.objects.all()
            #MyModel.objects.filter(pk=some_value).update(field1='some value')
             return HttpResponse("loads")