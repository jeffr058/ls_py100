# Write a function that compares the length of two strings. It should return -1 if the first string is shorter, 1 if the second string is shorter, and 0 if they're of equal length. For example:

# my solution
def compare_by_length(str1, str2):
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    elif len(str1) == len(str2):
        return 0
    
print(compare_by_length('patience', 'perseverance'))
print(compare_by_length('strength', 'dignity'))
print(compare_by_length('humor', 'grace'))
# end of my solution

compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0