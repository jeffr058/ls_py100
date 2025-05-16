# What will the following code do and why? Don't run it until you have tried to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# My solution
It will print 7 because passing a as the function argument passes its value and not the variable itself. The global variable a is unaffected by the function.

After reviewing the LS solution, I am noting that integers are immutable so the expression in the function creates a new object.