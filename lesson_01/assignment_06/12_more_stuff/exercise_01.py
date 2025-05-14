# What does the following function do? Be sure to identify the output value.

# def do_something(dictionary):
#     return sorted(dictionary.keys())[1].upper()

# my_dict = {
#     'Karl':     108,
#     'Clare':    175,
#     'Karis':    140,
#     'Trevor':   180,
#     'Antonina': 132,
#     'Chris':    101,
# }

# print(do_something(my_dict))

The keys method creates a view object of the dictionary keys. The sorted function passes the view object and creates a new list of the keys and sorts it (alphabetically). It then returns the value at the index 1 position in uppercase letters. The output will be 'CLARE'.