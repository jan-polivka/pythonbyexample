# Define a class simply so
class Person:
# A class variable can be declared as such
    name = "Person"
    age = 0

# The constructor for the class
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Despite the constructor accepting three arguments,
# the method gets called only with two arguments
        
# Note that functions that belong to a class are called methods.

# A class method can be declared as such
    def hello(self):
        print("Hello", self.name)
# A static method can be declared as such
    @staticmethod
    def get_species():
        return "Homo Sapiens"
    
# To create a new instance of the class, simply call
person = Person("John", 30)

# To call a method, simply use the dot operator
person.hello()
    