from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    # Главная страница
    path('records/', views.index, name='index'),
    path('records/contract_add/', views.contract_add, name='contract_add'),
    path('records/contract_edit/<int:record_id>/', views.contract_edit, name='contract_edit'),
]
