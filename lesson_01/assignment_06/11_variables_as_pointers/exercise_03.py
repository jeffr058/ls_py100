# Without running this code, what will it print? Why?

# dict1 = {
#     "Hitchhiker's Guide to the Galaxy": 42,
#     'Monty Python': 'The Life of Brian',
#     'Airplane!': "Don't call me Shirley!",
# }

# dict2 = dict(dict1)
# dict2['Monty Python'] = 'Holy Grail'
# print(dict1['Monty Python'])

It will print 'Holy Grail' as the value.

By passing dict1 to the dict constructor, dict2 points to a shallow copy. dict2 is a new container that copied the references to the objects in dict1 and not new objects, meaning any changes to the mutable objects will be reflected in both dict1 and dict2.