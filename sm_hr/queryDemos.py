#***(1)Returns all employees from employee table
employees = Employee.objects.all()

#(2)Returns first employee in table
firstEmployee = Employee.objects.first()

#(3)Returns last employee in table
lastEmployee = Employee.objects.last()

#(4)Returns single employee by name
employeeByName = Employee.objects.get(employee="Hr Admin")

#***(5)Returns single employee by name
employeeById = Employee.objects.get(id=1)

#***(6)Returns all orders related to employee (firstEmployee variable set above)
firstEmployee.order_set.all()

#(7)***Returns orders employee name: (Query parent model values)
attendace_first = Attendance.objects.first()
parentName = attendace_first.employee.employee

#(8)***Returns products from products table with value of "Out Door" in category attribute
attendace_filter = Attendance.objects.filter(status="Present")

#(9)***Order/Sort Objects by id
leastToGreatest = Attendance.objects.all().order_by('id')
greatestToLeast = Attendance.objects.all().order_by('-id')


#(10) Returns all products with tag of "Sports": (Query Many to Many Fields)

'''
(11)Bonus
Q: If the employee has more than 1 ball, how would you reflect it in the database?
A: Because there are many different products and this value changes constantly you would most 
likly not want to store the value in the database but rather just make this a function we can run
each time we load the employees profile
'''

#Returns the total count for number of time a "Ball" was ordered by the first employee
attendance_present = firstEmployee.attendance_set.filter(status="Present").count()
attendance_absent = firstEmployee.attendance_set.filter(status="Absent").count()

#Returns total count for each product orderd
allAttendance = {}

for attendace_first in firstEmployee.attendance_set.all():
	if attendace_first.attendance_id in allAttendace:
		allAttendace[attendace_first.id] += 1
	else:
		allAttendace[attendace_first.id] = 1

#Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(Employee)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()

# attendance = employeeByName.attendance_set.all()