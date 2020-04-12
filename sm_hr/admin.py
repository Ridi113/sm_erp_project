from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(BloodGroup)
admin.site.register(Religion)
admin.site.register(Gender)
admin.site.register(GroupOfCompany)
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Section)
admin.site.register(Country)
admin.site.register(Division)
admin.site.register(District)
admin.site.register(Employee)
admin.site.register(EmployeePersonalInformation)
admin.site.register(Attendance)