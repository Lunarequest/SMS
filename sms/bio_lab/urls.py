from django.urls import path
from . import views

app_name = 'bio_lab' 

urlpatterns = [
    path('/save', views.save, name='save'),
    path('broken/<int:bio_eq_id>', views.broken, name='broken_with_pk'),
    path('delete/<int:bio_eq_id>', views.delete, name='delete_with_pk'),
    path('/edit', views.display, name="edit"),
    path('',views.console, name='bio_lab'),
]