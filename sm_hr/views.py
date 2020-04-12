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


def attendance(request):
    attendance = Attendance.objects.all()

    return render(request, 'sm_hr/attendance.html', {'attendance': attendance})
