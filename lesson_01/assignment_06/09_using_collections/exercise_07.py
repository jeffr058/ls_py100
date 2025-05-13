# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# Try this problem using the methods you've learned about in this chapter. Once you have that working, use the Python documentation for the str type to find an alternative solution.

my_list = info.split(':')
print(my_list)
info2 = '+'.join(my_list)
print(info2)


# Alternative solution

alt_info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
alt_info2 = alt_info.replace(':', '+')
print(alt_info2)