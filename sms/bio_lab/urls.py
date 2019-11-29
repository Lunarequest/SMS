from django.urls import path
from . import views

urlpatterns = [
    path('/edit', views.edit, name='edit'),
    path('/save', views.save, name='save'),
    path('',views.console, name='bio_lab'),
]