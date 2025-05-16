# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# My solution
It will print 2 because the global variable a is being accessed through the global keyword. Then, any reassignment of the variable will affect the global variable.