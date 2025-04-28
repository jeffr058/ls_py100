# Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

# $ python multiply.py
# Enter the first number: 3.1416
# Enter the second number: 2.7183
# 3.1416 * 2.7183 = 8.53981128

def multiply(num1, num2):
    result = num1 * num2
    return result
 
def get_num(prompt):
    num = input(prompt)
    return float(num)
    
input_num1 = get_num('Enter the first number: ')
input_num2 = get_num('Enter the second number: ')
product = multiply(input_num1, input_num2)
print(f'{input_num1} * {input_num2} = {product}')

