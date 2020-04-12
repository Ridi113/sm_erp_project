from django.forms import ModelForm
from .models import Employee, Attendance


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
