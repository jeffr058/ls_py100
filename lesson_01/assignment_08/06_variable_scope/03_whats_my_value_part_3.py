# What will the following code do and why? Don't run it until you have tried to answer.

def my_function():
    a = 1

    if True:
        print(a)

my_function()

# My solution
It will print 1 because the variable a is accessible inside the if statement. Then, True is truthy so the code block of the if statement will be executed. 