from django.urls import path
from . import views

urlpatterns = [
    path('bio', views.console, name='bio_lab')
]