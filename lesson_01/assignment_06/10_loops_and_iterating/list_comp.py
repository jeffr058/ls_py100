cats_colors = {
    'Tess': 'brown',
    'Leo': 'orange',
    'Fluffy': 'gray',
    'Ben': 'black',
    'Kat': 'orange',
}

names = [ name.upper() 
         for name in cats_colors
         if name[0] == 'L' 
         and cats_colors[name] == 'orange' ]
print(names)