from django.db import models
import uuid
from django.contrib.auth.models import User
from datetime import datetime
# from django_serializable_model import SerializableModel


# class BloodGroup(SerializableModel):
class BloodGroup(models.Model):
    blood_group_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.blood_group_name}'

class Religion(models.Model):
    religion_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.religion_name}'

class Gender(models.Model):
    CATEGORY = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.gender_name}'

class GroupOfCompany(models.Model):
    group_of_company_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    remarks = models.CharField(max_length=300, null=True, blank=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.group_of_company_name}'

class Company(models.Model):
    company_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    group_of_company = models.ForeignKey(GroupOfCompany, on_delete=models.CASCADE, null=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    company_logo = models.ImageField(upload_to='photo', null=True, blank=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.company_name}'

class Department(models.Model):
    department_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.department_name}'

class Designation(models.Model):
    designation_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.designation_name}'

class Section(models.Model):
    section_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.section_name}'

class Country(models.Model):
    country_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.country_name}'

class Division(models.Model):
    division_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.division_name}'

class District(models.Model):
    district_name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.district_name}'

class Employee(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    employee_id = models.CharField(max_length=50, null=False, blank=False, unique=True)
    employee = models.CharField(max_length=225, null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    joining_date = models.DateTimeField(null=False, blank=False)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)

    def __str__(self):
        return f'{self.employee, self.designation, self.department}'

class EmployeePersonalInformation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='photo/', blank=True)
    Father_name = models.CharField(max_length=225, null=False, blank=False)
    Mother_name = models.CharField(max_length=225, null=False, blank=False)
    personal_mobile_number = models.CharField(max_length=17, null=False, blank=False, unique=True)
    alternate_mobile_number = models.CharField(max_length=17, null=False, blank=True)
    date_of_birth = models.DateField(null=False, blank=False, default='1900-01-01')
    national_id = models.CharField(max_length=20, null=False, blank=False, unique=True, default='')
    passport_number = models.CharField(max_length=20, null=False, blank=True, unique=True)
    passport_expiry_date = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, null=True)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, null=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    present_address = models.TextField(max_length=300, null=True, blank=True)
    permanant_address = models.TextField(max_length=300, null=True, blank=True)
    email = models.EmailField(null=False, blank=True, unique=True)
    remarks = models.CharField(max_length=300, null=True, blank=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)

    def __str__(self):
        return f'{self.employee}'

class Attendance(models.Model):
    STATUS = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    att_date = models.DateField(null=False, blank=False, default=datetime.now)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    time_in = models.TimeField(null=False, blank=True, default=datetime.now)
    time_out = models.TimeField(null=False, blank=True, default=datetime.now)
    remarks = models.CharField(max_length=100, null=True, blank=True)
    create_time = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    update_time = models.DateTimeField(null=False, blank=False, auto_now=True)

    def __str__(self):
        return f'{self.employee, self.att_date, self.status, self.time_in, self.time_out}'


