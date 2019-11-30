from django.urls import path
from . import views

app_name = 'physics' 

urlpatterns = [
    path('save', views.save, name='save'),
    path('/edit', views.display, name='edit'),
    path('edit/<int:bio_eq_id>', views.edit, name='edit_with_pk'),
    path('broken/<int:bio_eq_id>', views.edit, name='broken_with_pk'),
    path('delete/<int:bio_eq_id>', views.edit, name='delete_with_pk'),
    path('',views.console, name='physics'),
]