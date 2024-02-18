from classes_udc_employee import Employee
from classes_udc_project import Project

p = Project("Django app", 20000,"Globomantics")
e = Employee("Ji-Soo", 38, 1000, p)
print(e.project)
