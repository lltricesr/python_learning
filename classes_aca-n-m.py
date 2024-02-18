"""
Pillars of OOP
Abstraction -   display only basic information and hidding implementation details; only the interface
Encapsulation - 1. class instance should group related data and methods in 1 logic unit 2. Hiding of data attribute which are only used for internal implementation purposes (internal use only)
#   access modifiers is how other lang use but Python doesn't follow that strict. 
#   convention to make something private is the use of _varName; this indicates to outside users that it intent is internal only
Inheritance [compisition] - "is-a" relationship; inherit characteristics from the base; base class -> derivied class; parent -> child; superclass -> subclass
Polymorphism - one thing that can take on many forms; overriding -> name the same in the child as parent

File extension: _aca-n-m -> Accessing Class Attributes and Methods Module
Module Topics:
1. Classes Are Objects Too
2. Defining Class Methods

Functions and Classes a new object is allocated in memory

s = 'hello'     # str class instance; s -> name or identifier to work with object in memory

def fun():      # function class instance; fun -> name or identifier
    pass

class Employee: # type class instance; Employee -> name or identifier
    pass
    
Class Methods are a good use for factory methods; alternative constructors

Class Static Methods -> @staticmethod do not recieve an implicit first argument; no relation with class; utility methods
"""
from datetime import date   #from module import class -> importing a class for use

class Employee:
    #Class attribute -> a variable that will be accessible across all derived class
    minimum_wage = 1000

    #Class method -> a method that is ran on the class and doesn't recieve an instance as self parameter
    #cls -> Class itself
    @classmethod
    def change_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("Company is bankrupt.")
        #Use cls instead of the actual Class name {Employee} to make it dynamic; if Class Name change method will still work
        cls.minimum_wage = new_wage

    """
    use case -> employee hired only provides name & date of birth (dob) w/ minimum wage as salary
    input:
        name
        date of birth (dob)
    process:
        calculate dob
        set starting salary
    output:
        instance of Employee of new employee
    """
    @classmethod
    def new_employee(cls, name, dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, cls.minimum_wage)

    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    #Referred to as an instance method; method will recieve an instance as self parameter
    def increase_salary(self,percent):
        self.salary += int(self.salary * (percent/100))

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError("Minimum wage is ${Employee.minimum_wage}")
        self._salary = salary

e = Employee.new_employee("Mary", date(1991, 8, 12))
print(e.name)
print(e.age)
print(e.salary)

"""
print(Employee.minimum_wage)
Employee.change_minimum_wage(200)
print(Employee.minimum_wage)

Returns a mappingproxy -> a read-only dictionary
methods are Attributes in the Class' dictionary of an object type
{
    '__module__': '__main__', 
    '__init__': <function Employee.__init__ at 0x100698c20>, 
    'increase_salary': <function Employee.increase_salary at 0x100698cc0>, 
    'salary': <property object at 0x10068b6f0>, 
    '__dict__': <attribute '__dict__' of 'Employee' objects>, 
    '__weakref__': <attribute '__weakref__' of 'Employee' objects>, 
    '__doc__': None
}
#print(Employee.__dict__)    #Class internal attributes

e = Employee("Ji-Soo", 38, 1000)
print(e.minimum_wage)           #has access to the class attribute; using the attribute look-up chain -> look in instance attributes then class
print(Employee.minimum_wage)

#Use the dictionary to access the value of attributes in the instance
#Function parameters (Instance, MethodInputValue)
Employee.__dict__["increase_salary"](e,20)
print(e.salary)
"""