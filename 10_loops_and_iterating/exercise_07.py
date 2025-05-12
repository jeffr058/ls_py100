# Write a find_integers function that returns a list of all the integers from my_tuple:

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(my_tuple):
    int_list = [ obj for obj in my_tuple if type(obj) is int ]
    return int_list

integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]

# You can use the expression type(object) is int to determine whether an object is an integer. For instance:

# print(type(True) is int)      # False (boolean)
# print(type([1, 2, 3]) is int) # False (list)
# print(type(3.141592) is int)  # False (float)
# print(type(77) is int)        # True

# You may receive a SyntaxWarning warning message from the last two examples. You can ignore that warning.