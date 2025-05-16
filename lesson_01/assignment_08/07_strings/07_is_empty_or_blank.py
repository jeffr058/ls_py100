# Write an is_empty_or_blank function to determine whether a string is either empty or consists entirely of spaces. For example:

def is_empty_or_blank(string):
    return not string.strip(' ')  # LS solution

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

# My initial solution below didn't take into account whether the whole string consists entirely of spaces:
# return not string or ' ' in string