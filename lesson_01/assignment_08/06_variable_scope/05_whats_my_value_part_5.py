# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

# My solution
It will raise an error. The Python interpreter scans the whole function when it is defined and recognizes that a is being assigned a value (i.e., being initialized) and creates a new local variable. When the function is called, and the interpreter had already noted the local variable when it read the definition, so it expects the local variable to be initialized before it is accessed.