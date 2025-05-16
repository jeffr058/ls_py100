# Write a function that checks whether a string is empty or not. For example:

def is_empty(string):
    # return True if string == '' else False  # My solution
    return not string                         # Simpler LS solution

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True