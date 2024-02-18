"""
Pillars of OOP
Abstraction -   display only basic information and hidding implementation details; only the interface
Encapsulation - 1. class instance should group related data and methods in 1 logic unit 2. Hiding of data attribute which are only used for internal implementation purposes (internal use only)
#   access modifiers is how other lang use but Python doesn't follow that strict. 
#   convention to make something private is the use of _varName; this indicates to outside users that it intent is internal only
Inheritance [compisition] - "is-a" relationship; inherit characteristics from the base; base class -> derivied class; parent -> child; superclass -> subclass
Polymorphism - one thing that can take on many forms; overriding -> name the same in the child as parent

File extension: _ici -> Implementing Class Inheritance Module
Module Topics:
1. Introducing Class Inheritance
2. Overriding Parent Class Instance Methods
3. Inspecting Class Relationships
4. Extending Parent Class Instance Methods with super
5. Adding New Attributes to the Subclass Instances
6. Optimizing Memory with Slots
7. Multiple Inheritance and Method Resolution Order

Don't Repeat Yourself (DRY) - Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

All class implicitly inherit from object; object is a superclass of all class
    class CustomClass(object):
Object contains all dunder methods
When adding our on custom during methods

Multiple Inheritance -> inherit from multiple class; viewed as an anti-pattern
Trades is use in places for multiple inheritance
Mixin Classes allow for multiple inheritance for subclass when there will be a lot of instantiations. 
"""

class Employee:
    #implementing slots in the base class will be for all derived
    #if slots is not done in superclass; the __dict__ from it will be inherited; therefore slots should be defined in the super
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self,percent):
        self.salary += int(self.salary * (percent/100))

    #self exploration: created function as a shortcut for self
    def salary_info(self):
        print(f"{self.name} has a monthly salary of ${self.salary}.")

#Inheritance is given by adding the base class in parenthesis after the derived class name
#now the subclass has all the methods and properties of the superclass
class Tester(Employee):
    def run_test(self):
        print(f"Testing is started by {self.name}...")
        print("Test are done.")

class Developer(Employee):
    #inheritance -> only need to account for attributes not in the base class in the derived class
    __slots__ = ("framework",)      #an iterable must a list therefore a 1 item list still has to contain a comma by definition. 

    #Adding attributes to a sub class
    #override the __init__ like any other
    def __init__(self, name, age, salary, framework) -> None:
        super().__init__(name, age, salary)
        self.framework = framework
    
    #this is called overriding; this function will be called in place of the method in the base class; impacts mro
    def increase_salary(self, percent, bonus=0):
        #Never use: self.increase_salary -> this will cause an infinite loop because mro will just recall this method
        super().increase_salary(percent)   #super().method is a subclass call to the superclass to use its implementation
        #Employee.increase_salary()         #super() replaces this; super() is more dynamic and follows the guardrailes of mro
        self.salary += bonus

def print_divider():
    print('-' * 20)

employee1 = Tester("Lauren", 44, 1000)
employee2 = Developer("Ji-Soo", 38, 1200, "Flask")

print(employee2.name)
print(employee2.framework)

"""
#isinstance(Instance, Class)                #True if the Instance was instantiated from the Class
print(isinstance(employee1, Tester))        #True; employee1 is an instance of Tester
print(isinstance(employee1, Employee))      #True: employee1 is an instance of Employee thru inheritance via derived class Tester

#issubclass(SubClass, SuperClass)           #True if SubClass is-a derived class from the SuperClass or a derived class in its heirarchy
print(issubclass(Developer, Employee))      #True; Developer class is a direct subclass of the Employee superclass
print(issubclass(Employee, object))         #True; Employee class is-a derived class from the object class as-is all classes
print(issubclass(Developer, object))        #True; Developer class is-a derived class from the object class as a derived class in its heirarchy

#This heirarchy is prevelant with the Exception class; it can be used for the handling of errors specifically; E.g.,
try:
    # something that raises the FloatingPointError or the ZeroDivisionError
    raise FloatingPointError("Watch out, a floating point error!")
except ArithmeticError as e:        # ArithmeticError is a superclass of both the FloatingPointError & ZeroDivisionError
    # handle this error
    print(e)

employee1.salary_info()
employee2.salary_info()
employee1.increase_salary(20)
employee2.increase_salary(20,30)
employee1.salary_info()
employee2.salary_info()

employee1.run_test()
"""