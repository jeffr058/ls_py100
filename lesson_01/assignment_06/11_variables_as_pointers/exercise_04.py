# Without running this code, what will it print? Why?

# dict1 = {
#     'a': [1, 2, 3],
#     'b': (4, 5, 6),
# }

# dict2 = dict(dict1)
# dict1['a'][1] = 42
# print(dict2['a'])

It will run [1, 42, 3] because the value for 'a' is mutable, meaning the shallow copy of dict1 will reference the original object in memory. Mutating the object will affect all collections that contain that object.