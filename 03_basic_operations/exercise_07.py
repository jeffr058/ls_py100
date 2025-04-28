# What will the following code do? Why?

# int('3.1415')

It will result in 3. The int typecast function loses the values after the decimal, effectively rounding down to the nearest whole number.

# Correct answer:

It will result in an error because the float in the argument is a string literal, but it must be an integer for int() to work.