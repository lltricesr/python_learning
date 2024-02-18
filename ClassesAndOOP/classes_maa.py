"""
Pillars of OOP
Abstraction -   display only basic information and hidding implementation details; only the interface
Encapsulation - 1. class instance should group related data and methods in 1 logic unit 2. Hiding of data attribute which are only used for internal implementation purposes (internal use only)
#   access modifiers is how other lang use but Python doesn't follow that strict. 
#   convention to make something private is the use of _varName; this indicates to outside users that it intent is internal only

File extension: _maa -> Managing Attribute Access Module
Module Topics:
1. Validating Attributes Values
2. Encapsulation and Name Mangling
3. Accessing Attributes though Properties
4. Setting Property Values
5. Using Computed Properties
"""

class Employee:
    def __init__(self, name, age, position, salary) -> None:
        # python does not use access modifiers; trust the user; use convention _attr_name (leading _) means that it is private, but still accessible; user should not ignore 
        # use name mangling to make it harder __attr_name (double underscore), outside the Class the full name will be __ClassName__attr_name; still accessible but harder and intentional
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary        #contains the montly ammount
        self._annual_salary = None  #this is initialize a private property for caching
        #self.annual_salary = salary * 12    # salary for the year; not a good practice as this would need to be changed too. 
        #self.set_salary(salary)

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

    """
    #getters and setters not to allow access directly to _salary 
    #getter & setters is an antipattern as new get & set will cause new code
    #def get_salary(self):
    """
    #Making getter & setters backwards compatible using a function decorator; decorate w/o need of additional code
    #property decorator changes the method to a property 
    @property
    def salary(self):
        # return f"${self.salary}"      #if you wanted to format return
        # return round(self.salary, 2)
        # logging.info("Someone access the salary")
        return self._salary     #this is an exercise of encapsulation; this attribute only accessible internally to the class
    
    #to set the setter of a property needs the setter decorator
    #using the setter the decorator @salary; setter method salary and the @property salary need to be the same
    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        #monly salary changed so reset _annual_salary from cached value
        self._annual_salary = None
        self._salary = salary

    #Computed property; property based on a computation
    @property
    def annual_salary(self):
        #using the cached value I can now set a check
        if self._annual_salary is None:     #the value at instantiation of the object; only calculated 1 time
            self._annual_salary = self.salary * 12
        return self._annual_salary

    # hybrid properties used in SQLAlchemy
    # @hybrid_property used with database 
    
    """
    #Read-only property
    #Raise an error inside of the setter method -OR- leave out the setter completely
    @property
    def attr(self):
        return self._attr
    @attr.setter
    def attr(self, value):
        raise AttributeError("Attr is read-only")

    #Write-only proeprty
    #Raise an error inside of the 'getter' method
    @property
    def attr(self):
        raise AttributeError("Attr is write-only")
    @attr.setter
    def attr(self, value):
        self._attr = value
    #This is good for passwords when you want to enforce a hash on the password before storing it.
    """

def print_divider():
    print('-' * 20)

employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1000)

print(employee1.annual_salary)
employee1.salary = 1000
print(employee1.annual_salary)

"""
print(employee1.annual_salary)      #only calculated when it is needed; helps when a big computation you will want to cache
employee.salary         #this will use the getter with @property and allows backwards compatibilty when user thinks they are calling the actual property. 
employee1.salary()      #this is necessary if the @property is not used
employee.set_salary(2000)       #this is an execise of abstraction, the implementation of the salary minimum is hidden.

allowing direct assignment would skip the
employee1.salary = 200      #this would skip the validation and directly access the property 

this would be bad design
user_input = int(input("Input salary: "))
if user_input < 1000:
    raise ValueError('Minimum wage is $1000')
else:
    employee1.salary = user_input
"""