# What will the following code do and why? Don't run it until you have tried to answer.

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# My solution
It will print [10, 2, 3] because the global variable is being accessed in the function to mutate its value, not to attempt to reassign the variable.