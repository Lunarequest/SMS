from django.urls import path
from . import views
urlpatterns = [
    path('select', views.auth, name='select'),
]
