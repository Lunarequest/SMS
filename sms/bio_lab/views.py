from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def console(request):
    response = HttpResponse('works')
    return response