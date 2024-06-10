# stock/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chart/', views.stock_chart, name='stock_chart'),
]