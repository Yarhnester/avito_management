from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),
]
