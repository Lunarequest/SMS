from django.urls import path
app_name = 'library'
urlpatterns = [
    path('', views.console, name='library')
]
