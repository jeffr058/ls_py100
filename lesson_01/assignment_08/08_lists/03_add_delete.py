# We are given the following list of energy sources.

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']

# Write some code to remove 'fossil' from the list, then add 'geothermal' to the end of the list.

energy.pop(0)
energy.append('geothermal')

print(energy)

# After review of the LS solution, I'm noting that the remove method is better if I don't know whether a given element is in the list.