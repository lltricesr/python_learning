"""
Pillars of OOP
Abstraction -   display only basic information and hidding implementation details; only the interface
Encapsulation - 1. class instance should group related data and methods in 1 logic unit 2. Hiding of data attribute which are only used for internal implementation purposes (internal use only)
#   access modifiers is how other lang use but Python doesn't follow that strict. 
#   convention to make something private is the use of _varName; this indicates to outside users that it intent is internal only

File extension: _icc -> Instantiating Custom Classes Module
Module topics:
1. Objects are Dictionaries
2. Classes and Instances
3. Passing Self to instance Methods
4. Turning Instances to Strings
5. Modifying Instance Representation
6. Overview of Special Dunder Methods
"""
# Name mangling - place 2 underscore __varName will require access of obj.__ClassName__varName
""" 
built in functions (Constructor): 
__new__ - allocate mem for a new object and send it to the __init__ function
__init__ - receive a new object from the __new__ function as "self" function
    programmer define this function
"""
class Employee:
    def __init__(self, name, age, position, salary) -> None:
        """
        self.__dict__['name'] = "Ji-Soo"
        self.__dict__['age'] = 38
        self.__dict__['developer'] = 'developer'
        self.__dict__['salary'] = 1200
        Is the same as...
        """
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self,percent):
        self.salary += int(self.salary * (percent/100))
    
    # replaced by the __str__
    def info(self):
        print(f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}")

    # dunder method - method with Double UNDERscore - Special method names on Python
    # interface with objects
    # built-in function (override)
    # readable string representation
    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of {self.salary}"
    
    # built in function (override)
    # represent an object - wrapper method - formal way of presentation to developer
    # not meant to be descriptive, so that the object could be used to instantiate an object: example, Employee("Ji-Soo", 38, "developer", 1200) 
    # this should follow the order of the __init__ func
    # Python style guide suggest that line continuation separation be done in ()
    def __repr__(self) -> str:
        return (
            f"Employee("
            f"{repr(self.name)}, {repr(self.age)}, "
            f"{repr(self.position)}, {repr(self.salary)})"
        )

    # Getter - used for consistency as it just returns the value
    def get_salary(self):
        # return f"{self.salary}"   # this will return the salary back as a dollar amount to ommit the need for the caller to format
        # return round(self.salary, 2)  # using a decimal class
        # logging.info("Someone accessed the salary attribute.")    #used for logging analytics
        return self._salary
    
    # Setter - used to perform action on the value before assignment
    # in this example it would block the setting of salary below a minimum wage
    def set_salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._salary = salary

    """
    in order for your class to support the + operator you will need to override the dunder method __add__
    """

def print_divider():
    print('-' * 20)

# e = Employee()
# print(e.__dict__)     # all objects have are made up of dictionary
# print(e.__class__)    # this is a function to call to get the class of an object

employee1 = Employee("Ji-Soo", 38, "developer", 1200)           # rather than calling it an object, call it an instances as they are instantiation of Employee
employee2 = Employee("Lauren", 44, "tester", 1000)

print(employee1.name)
print(employee2.name)
print_divider()
employee1.info()
employee1.increase_salary(20)
employee1.info()
print_divider()
employee1.info()
print_divider()
print(str(employee2))  # str() - calls the __str__ built-in function of an object
print_divider()
# eval() - evaluate a string and returns an object
# print(str(eval(repr(employee2)))) # repr() - calls the __repr__ built-in function of an object
#employee2.set_salary(200) # this would cause a ValueError exception
employee2.set_salary(2000)
print(employee2.get_salary())