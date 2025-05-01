# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

stuff_1 = list(stuff)  # can use original name for list & new tuple
stuff_1[2] = 'goodbye'
stuff_1 = tuple(stuff_1)

print(stuff_1)
print(type(stuff_1))