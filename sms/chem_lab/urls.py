from django.urls import path
from . import views
app_name='chem_lab'
urlpatterns = [
    path('', views.edit, name='chem_lab'),
    path('/edit', views.edit, name="edit"),
    path('/add_con', views.add_con, name="add_chem"),
    path('/add_eq', views.add_eq, name='add'),
    path('edit_con/<int:consumable_id>', views.edit_con, name="editcon"),
    path('edit_eq/<int:chem_eq_id>', views.edit_eq, name='editeq'),
    path('broken/<int:chem_id>', views.broken, name='broken_with_pk'),

]
