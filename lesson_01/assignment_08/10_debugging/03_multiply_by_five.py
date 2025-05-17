# When the user inputs 10, we expect the program to print The result is 50!, but that's not the output we see. Why not?

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())

print(f"The result is {multiply_by_five(number)}!")

# The value of the user input is a string, so '10' * 5 will multiply the string 5 times.