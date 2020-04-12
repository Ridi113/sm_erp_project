
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views



from sm_hr import views

urlpatterns = [
    path('', views.home, name="home"),
    path('employee/', views.employee, name='employee'),
    path('attendance/<str:pk_test>/', views.attendance, name="attendance"),
    ]