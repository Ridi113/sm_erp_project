from django.shortcuts import render
from  django.http import HttpResponse
def home(request):
    return HttpResponse('Hello, World!')

# Create your views here.


def home(request):
    return render(request, 'sm_hr/dashboard.html')

def employee(request):
    # return HttpResponse("Employee page")
    return render(request, 'sm_hr/employee.html')

def attendance(request):
    return render(request, 'sm_hr/attendance.html')