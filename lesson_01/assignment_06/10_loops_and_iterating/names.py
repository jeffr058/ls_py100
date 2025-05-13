names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name == 'Max':
        continue

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)