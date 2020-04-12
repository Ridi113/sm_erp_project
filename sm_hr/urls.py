
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views



from sm_hr import views

urlpatterns = [
    path('', views.home),
    path('employee/', views.employee),
    path('attendance/', views.attendance),
    ]