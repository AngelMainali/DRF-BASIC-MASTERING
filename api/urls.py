
from django.urls import path
from .import views

urlpatterns = [
    path('students/', views.StudentsView, name='students'),
    path('students/<int:pk>/', views.StudentsDetailView, name='studentsDetail'),
    path('employee/', views.EmployeeView.as_view(), name='employee'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employeeDetail'),

]
