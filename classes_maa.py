# _maa -> Managing Attribute Access Module
"""
Pillars of OOP
Abstraction -   display only basic information and hidding implementation details; only the interface
Encapsulation - 1. class instance should group related data and methods in 1 logic unit 2. Hiding of data attribute which are only used for internal implementation purposes (internal use only)
#   access modifiers is how other lang use but Python doesn't follow that strict. 
#   convention to make something private is the use of _varName; this indicates to outside users that it intent is internal only

"""
class Employee:
    def __init__(self, name, age, position, salary) -> None:
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self,percent):
        self.salary += int(self.salary * (percent/100))

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}"
    
    def __repr__(self) -> str:
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        )

    def get_salary(self):
        return self._salary
    
    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._salary = salary

def print_divider():
    print('-' * 20)

employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

print(repr(employee1))