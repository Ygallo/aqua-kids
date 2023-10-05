from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('timetable/', views.timetable, name='timetable'),
    path('contact_us/', views.contact_us, name='contact_us'),
]
