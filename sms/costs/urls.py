from django.urls import path
from . import views
urlpatterns = [
    path('',views.student, name='student'),
    #path('paid/<int:student_id>', views.remove, name='remove_student'),
]
