from django.urls import path
from . import views

app_name = 'physics'

urlpatterns = [
    path('save', views.save, name='save'),
    path('/edit', views.display, name='edit'),
    path('edit/<int:phy_eq_id>', views.edit, name='edit_with_pk'),
    path('broken/<int:phy_eq_id>', views.broken, name='broken_with_pk'),
    path('delete/<int:phy_eq_id>', views.delete, name='delete_with_pk'),
    path('/add', views.add, name='add'),
    path('',views.console, name='physics'),
]
