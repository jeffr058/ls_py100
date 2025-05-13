# Using the code below, classify the identifiers as global, local, or built-in. For our purposes, you may assume this code is the entire program.

# def multiply(left, right):
#     return left * right

# def get_num(prompt):
#     return float(input(prompt))

# first_number = get_num('Enter the first number: ')
# second_number = get_num('Enter the second number: ')
# product = multiply(first_number, second_number)
# print(f'{first_number} * {second_number} = {product}')

multiply	    global
left	        local
right   	    local
first_number	global
second_number	global
get_num	        global
prompt	        local
float	        built-in
input	        built-in
product	        global
print	        built-in