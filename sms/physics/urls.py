from django.urls import path
from . import views

app_name = 'physics' 

urlpatterns = [
    path('save', views.save, name='save'),
    path('edit/<int:bio_eq_id>', views.edit, name='edit_with_pk'),
    path('',views.console, name='physics'),
]