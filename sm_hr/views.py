from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import EmployeeForm, AttendanceForm


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

    context = {'employee': employee, 'attendance': attendance, 'attendance_employee': attendance_employee,
               'attendance_count': attendance_count,
               'absent_count': absent_count}

    return render(request, 'sm_hr/attendance.html', context)


def createAttendance(request):
    form = AttendanceForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'sm_hr/attendance_form.html', context)


def createEmployee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'sm_hr/employee_form.html', context)


def updateAttendance(request, pk):
    attendance_id = Attendance.objects.get(id=pk)
    form = AttendanceForm(instance=attendance_id)

    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance_id)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'sm_hr/attendance_form.html', context)
