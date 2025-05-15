# Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'.

str1 = 'Captain Ruby'
str2 = str1.replace('Ruby', 'Python')

print(str1)
print(str2)

# practice with other two methods from LS solution
first_word = 'Captain Ruby'[:8]
second_word = 'Python'
new_str = first_word + second_word

word_list = 'Captain Ruby'.split()
first = word_list[0]
new_str1 = first + " " + second_word