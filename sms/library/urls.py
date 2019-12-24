from django.urls import path
from . import views
app_name = 'library'
urlpatterns = [
    path('', views.console, name='library'),
    path('issue/<int:book_id>', views.issue, name='issue_with_pk'),
    path('/add', views.add, name='add'),
    path('library/add', views.add, name='add'),
    path('delete/<int:book_id>', views.delete, name='delete'),
    path('return/<int:book_id>', views.return_book, name='return_with_pk'),
    path('add_id/<int:book_id>', views.add_copy_id, name='add_id_with_pk'),
]
