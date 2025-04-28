# Take a look at this code snippet:

# foo = 'bar'

# def set_foo():
#     foo = 'qux'

# set_foo()
# print(foo)

bar

foo is assigned a value in Line 1, and then another variable foo in the function scope is assigned, hiding the foo variable from Line 1. The code calls the set_foo function, which returns the assigned value qux, then prints bar.