
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views



from sm_hr import views

urlpatterns = [
    path('', views.home, name="home"),
    path('employee/', views.employee, name='employee'),
    path('attendance/<str:pk_test>/', views.attendance, name="attendance"),
    path('create_employee/', views.createEmployee, name="create_employee"),
    path('create_attendance/', views.createAttendance, name="create_attendance"),
    path('update_attendance/<str:pk>/', views.updateAttendance, name="update_attendance"),
    ]