from django.urls import path
from . import views

app_name = 'bio_lab' 

urlpatterns = [
    path('/save', views.save, name='save'),
    path('broken/<int:bio_eq_id>', views.broken, name='broken_with_pk'),
    path('edit/<int:bio_eq_id>', views.edit, name='edit_with_pk'),
    path('delete/<int:bio_eq_id>', views.delete, name='delete_with_pk'),
    path('/edit', views.display, name="edit"),
    path('/add', views.add, name='add'),
    path('',views.console, name='bio_lab'),
]