"""
Pillars of OOP
Abstraction -   display only basic information and hidding implementation details; only the interface
Encapsulation - 1. class instance should group related data and methods in 1 logic unit 2. Hiding of data attribute which are only used for internal implementation purposes (internal use only)
#   access modifiers is how other lang use but Python doesn't follow that strict. 
#   convention to make something private is the use of _varName; this indicates to outside users that it intent is internal only
Inheritance [compisition] - "is-a" relationship; inherit characteristics from the base; base class -> derivied class; parent -> child; superclass -> subclass
Polymorphism - one thing that can take on many forms; overriding -> name the same in the child as parent

File extension: _udc -> Using Data Classes Module
Module Topics:
1. Introducting Data Classes
2. Type Hinting of Instance Attributes
3. Implementing Slots and Methods
4. What's Next?

Classess require the management of methods {such as __init__ to add attributes, __repr__ to present the data}

What if you just need a data container? -> avoiding boiler plate code

class Project:
    def __init__(self, name, payment, client) -> None:
        self.name = name            #name of prject
        self.payment = payment      #payment that we get for finishing
        self.client = client        #name of client request
    
    def __repr__(self) -> str:
        return f"Project(name={repr(self.name)}, payment={repr(self.payment)}, client={repr(self.client)})"

Python is dynamically type

Use mypy as a type checker -> Syntax: mypy class.py

Python Best Practices

What's Next
    Design Patterns
    SOLID principles
    Abstract classes -> don't create instances; interfaces
    Docstrings
    Metaclasses
    Descriptors
    Decorators

Large projects -> split the class into different files and import them
This will be better for presentation and beauty when dealing with many classes
E.g.,
    classes_udc_project.py
    classes_udc_employee.py
    classes_udc_main.py
"""
#Introducing the Data Class
from dataclasses import dataclass
#Avoid required type hints
from typing import Any

#data class decorator -> avoids the boiler plate code; use for simple classes
#after Python 3.10v -> to implement Slots to data classes
#Inheritance works in the same way
@dataclass(slots=True)
class Project:
    #the __init__ & wrapper methods {such as, __repr__} are created in the background
    #define each attribute for each instance
    name: str       #type hints -> are required for data class attribute to identify what type of value expected for the attribute
    payment: int    #Avoiding a type hint with the import of Any this can become -> payment: Any
    client: str

    #functions can be added as well; it doesn't have to only be data attributes
    def notify_client(self):
        print(f"Notifying the client about the progress of the {self.name}...")
    
class Employee:
    def __init__(self, name, age, salary, project) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        """
        Composition -> building a relationship between classes by assigning an instance of a class to an attribute of another class
        This is seldomly used in place of an (inheritance) is-a with a has-a relationship {E.g., Employee has-a project}
        Inheritance is a programming language feature whereas Composition is a design choice.
        """
        self.project = project

p = Project("Django app", 20000,"Globomantics")
e = Employee("Ji-Soo", 38, 1000, p)
print(e.project)
