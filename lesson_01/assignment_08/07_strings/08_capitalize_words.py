# Write code that capitalizes the words in the string 'launch school tech & talk', so that you get the string 'Launch School Tech & Talk'.

# 1
string = 'launch school tech & talk'

string.title()
print(string.title())

# 2
string1 = 'launch school tech & talk'
words = string1.split(' ')
cap_list = []

for word in words:
    cap_list.append(word.capitalize())

cap_string = ' '.join(cap_list)

print(cap_string)
