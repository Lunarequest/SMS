from django.urls import path
from . import views
app_name='chem_lab' 
urlpatterns = [
    path('', views.console, name='chem_lab'),
    path("edit_con/<int:consumable_id>", views.edit_con, name="editcon"),
    path('broken/<int:chem_id>', views.broken, name='broken_with_pk'),
    
]
