# Write a function that returns the last element of a list provided as an argument. For example:

def last(lst):
    return lst[-1] if lst else None

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))  # My test

# Be sure to handle the case where the input list is empty.