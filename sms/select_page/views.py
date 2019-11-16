from django.shortcuts import render

# Create your views here.
def auth(repuest):
    response = render(repuest,'select_page/page.html')
    return response