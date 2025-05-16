# What will the following code do and why? Don't run it until you have tried to answer.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# My solution
It will print 15 because it takes the variable value from the global scope and creates a new local variable with that value.