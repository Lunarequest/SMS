from django.urls import path
from . import views
urlpatterns = [
    path('', views.console, name='chem_lab'),
    path("edit", views.edit, name="edit")
]
