"""
Supplementary class for _ici module

Implementing __slots__ for optimizing memory
This will replace the __dict__ dunder method and make the listing of attributes more static

Syntax -> __slots__ = iterable

Advantages
    faster attribute access
    reduces memory overhead; each instance doesn't have to save an internal dictionary

Disadvantages
    can't create instance attributes dynamically; this is good when you want to prevent dynamic state attributing

CPython implements __slots__

Slots used heavily in SQLAlchemy 
"""
class Developer():
    #the iterable {e.g., tuple used here} must contain a list of all the instant attributes
    #this instructs new instances to be instantiated with slots rather than a dictionary
    __slots__ = ("name", "age", "salary", "framework")

    def __init__(self, name, age, salary, framework) -> None:
        self.name = name
        self.age = age
        self.salary = salary
        self.framework = framework

employee1 = Developer("Ji-Soo", 38, 1200, "Flask")

#print(employee1.__dict__)   #this will produce an error
print(employee1.__slots__)

#slots prevents creating attributes dynamically in the application.
#employee1.new_attribute = 'some_value'     #this would be a legal operation if __slots__ not used; 