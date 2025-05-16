# Write a function that returns the first element of a list provided as an argument. For example:

def first(list):
    return list[0] if list else None     # list changed from list != []

print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))                         # My test

# Be sure to handle the case where the input list is empty.