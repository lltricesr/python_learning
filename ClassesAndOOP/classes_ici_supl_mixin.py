"""
Supplementary class for _ici module

Mixin classes is a practical way of using multiple inheritance
"""
class Employee:
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self,percent):
        self.salary += int(self.salary * (percent/100))

#Mixin suffix is used as a practice to indicate that this class will be used for multiple inheritance; adding addition functionality
class SlotsInspectorMixin:
    #Remember -> all classes have an inherited __init__ and therefore contain an empty list of attributes
    #To ensure that Slots is enabled across all derived class of Developer
    #Implement Slots with an empty tuple
    __slots__ = ()
    #if this is True then the Class instance is implementing Slots
    def has_slots(self):
        return hasattr(self, "__slots__")   #hasattr(Instance, Attribute) -> built-in function that checks if the Instance contains the Attribute

"""
Multiple inheritance is provided by adding the Class(es) to the inheritance
The order of inheritance is based on listing right to left
Method Resolution Order -> is the defined order (use C3 algorithm) in which the method of execution will be search for in the inheritance tree
C3 algorithm -> look in subclass, then the superclass(es) {right to left} then further up the heirarchy until it reaches the top {object}
"""
class Developer(SlotsInspectorMixin, Employee):
    __slots__ = ("framework",)

    def __init__(self, name, age, salary, framework) -> None:
        #C3 algorithm used for super() omiting the subclass
        super().__init__(name,age,salary)
        self.framework = framework
    
    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus

    """
    It has been determined that there is a use case outside of this derived class to use this method.
    It could be moved to the SuperClass(Employee) but scope is even beyond that.
    This is where Mixin Classes are used and multiple inheritance is necessary.
    """
    """
    #Moved to Mixin Class
    #if this is True then the Class instance is implementing Slots
    def has_slots(self):
        return hasattr(self, "__slots__")   #hasattr(Instance, Attribute) -> built-in function that checks if the Instance contains the Attribute
    """

employee1 = Developer("Ji-Soo", 38, 1200, "Flask")
print(employee1.has_slots())
print(Developer.__mro__)    #this is a special method that will return the Method Resolution Order from the subclass in a tuple

"""
Caution: When using multiple inheritance it may introduce memory overhead if Slots are not taken care of.
print(employee1.__dict__)   #before implementing Slots in the Mixin Class this would be valid.
"""
