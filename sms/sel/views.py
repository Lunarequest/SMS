from django.shortcuts import render

# Create your views here.
def page(request):
    response = render(request,'sel/c.html')
    return response