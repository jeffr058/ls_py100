# Modify the greeter.py program to ask for the user's first and last names separately, then greet the user with their full name.

# $ python greeter.py
# What is your first name? Bob
# What is your last name? Roberts
# Hello, Bob Roberts!

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

print(f'Hello, {first_name} {last_name}!')