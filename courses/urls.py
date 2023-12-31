
from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_courses, name='courses'),
    path('<int:course_id>/', views.course_detail, name='course_detail'),
    path('categories/', views.course_categories, name='course_categories'),
    path('add/', views.add_course, name='add_course'),
    path('edit/<int:course_id>/', views.edit_course, name='edit_course'),
    path('course/<int:pk>/delete/', views.DeleteCourse.as_view(),
         name='delete_course'),
]
