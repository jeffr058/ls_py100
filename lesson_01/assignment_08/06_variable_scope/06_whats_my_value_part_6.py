# What will the following code do and why? Don't run it until you have tried to answer.

a = 1

def my_function():
    a = 2

my_function()
print(a)

# My solution
It will print 1 because the local variable initialized with the same name as a global variable shadows, or hides the existence of, the global variable in the function, being its own variable inside the function only.