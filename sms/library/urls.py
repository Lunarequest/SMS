from django.urls import path
from . import views
app_name = 'library'
urlpatterns = [
    path('', views.console, name='library'),
    path('issue/<int:book_id>', views.issue, name='issue_with_pk'),
    path('/add',views.add, name='add'),
    path('delete/<int:book_id>', views.delete, name='delete'),
]
