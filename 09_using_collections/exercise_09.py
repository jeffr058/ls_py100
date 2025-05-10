# Write some code to replace the value 6 in the following nested list with 606:

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

# You don't have to search the list. Just write an assignment that replaces the 6.

stuff[1][3] = 606
print(stuff)