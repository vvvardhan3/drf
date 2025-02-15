from django.urls import path
from . import views

urlpatterns = [
    path('students/',views.studentsView),
    path('students/<int:pk>/',views.studentDetailView),
    path('employees/',views.employees.as_view()),
    path('employees/<int:pk>/',views.employeesDetails.as_view()),
]