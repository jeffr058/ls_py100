# Without running this code, what will it print? Why?

# set1 = {42, 'Monty Python', ('a', 'b', 'c')}
# set2 = set1
# set1.add(range(5, 10))
# print(set2)

# Don't worry about having an exact match for the output. The important part is to show something that accurately represents set2.

set2 will print {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)} because assigning a variable to another variable doesn't create a new object but references the same object in memory.