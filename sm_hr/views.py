from django.shortcuts import render
from  django.http import HttpResponse
from .models import *


# Create your views here.


def home(request):
    attendance = Attendance.objects.all()
    employee = Employee.objects.all()

    total_employee = employee.filter(status="Active").count()

    total_attendance = attendance.count()
    present = attendance.filter(status='Present').count()
    absent = attendance.filter(status='Absent').count()

    context = {'attendance': attendance, 'employee': employee,
               'total_employee': total_employee, 'total_attendance': total_attendance,
               'present': present,
               'absent': absent}

    return render(request, 'sm_hr/dashboard.html', context)

def employee(request):
    # return HttpResponse("Employee page")
    employee = Employee.objects.all()

    return render(request, 'sm_hr/employee.html', {'employee': employee})


def attendance(request, pk_test):
    employee = Employee.objects.get(id=pk_test)
    attendance = Attendance.objects.all()

    attendance_employee = employee.attendance_set.all()
    attendance_count = attendance_employee.count()
    absent_count = attendance_employee.filter(status="Absent").count()

    context = {'employee': employee, 'attendance': attendance, 'attendance_employee': attendance_employee, 'attendance_count': attendance_count,
               'absent_count': absent_count}

    return render(request, 'sm_hr/attendance.html', context)
