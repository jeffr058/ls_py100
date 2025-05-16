# What will the following code do and why? Don't run it until you have tried to answer.

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# My solution
My guess is that the attempt to access the global variable b inside the function to reassign its list object follows the local variable rule and calling the function will raise an error while printing b will output the original, unaffected, list.