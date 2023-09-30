from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('students/', views.student, name='student'),
    path('student/add/', views.add_student, name='add_student'),
    path('student/edit/<int:student_id>/', views.edit_student, name='edit_student'),
    path('student/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]