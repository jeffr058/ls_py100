# What will the following code do and why? Don't run it until you have tried to answer.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# My solution
It will raise an error because it is trying to assign to a variable in a function, causing Python to treat it as a local variable that needs to be initialized with a value, and the value of x from the global variable is not accessible inside the function.