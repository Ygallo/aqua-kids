from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('student/', views.student, name='student'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]