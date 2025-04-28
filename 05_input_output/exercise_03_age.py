# Write a program named age.py that asks the user to enter their age, then calculates and reports the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 27 years old.

# How old are you? 27

# You are 27 years old.
# In 10 years, you will be 37 years old.
# In 20 years, you will be 47 years old.
# In 30 years, you will be 57 years old.
# In 40 years, you will be 67 years old.

age = int(input('How old are you? '))

print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')