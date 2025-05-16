# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()

# My solution
# It will print 1, because it is reading the value of the global variable a. It is then initializing the new local variable a.