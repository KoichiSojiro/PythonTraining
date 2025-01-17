'''
Created on Jul 25, 2016

@author: trannh08
'''
class Employee(object):
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return "$" + str(hours * 20.00)

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return "$" + str(hours * 12.00)
    #call a superclass's function
    def calculate_full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

my_employee = Employee("Nhan the Pig")
my_employee_wage = my_employee.calculate_wage(40)
print(my_employee.employee_name, "salary:", my_employee_wage)

my_pt_employee = PartTimeEmployee("Nhan Heo")
my_pt_employee_wage = my_pt_employee.calculate_wage(40)
my_ft_employee_wage = my_pt_employee.calculate_full_time_wage(40)
print(my_pt_employee.employee_name, "salary:", my_pt_employee_wage)
print(my_pt_employee.employee_name, "fulltime salary:", my_ft_employee_wage)

