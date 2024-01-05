# In Python, you can delare a variable simply so
my_var = "hello"

# You can also declare multiple variables at once
a, b, c = "a", "b", "c"

# As for types, Python is a dynamically typed language.
# This means that you don't have to declare the type
# and the type of a variable can be change throughout its lifetime.
my_var = 3

# To infer the type of a variable, you can use the
# type() function. For example:
print(type("string variable"))
print(type(350))
print(type(True))

# While Python does not have constants, that is variables
# that do not change, it is customary to declare them while
# in all caps
MY_CONSTANT = "should not change"