
from django.urls import path
from . import views


urlpatterns = [
    path('', views.course_categories, name='course_categories'),
]