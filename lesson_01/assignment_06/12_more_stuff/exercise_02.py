# Use the sqrt function from the math library to write some code that outputs the square root of 37. Try to write the code in three different ways.

#1
import math

def square_root(num):
    return math.sqrt(num)

print(square_root(37))  # 6.082762530298219
print()

#2
from math import sqrt

def square_root1(num):
    return sqrt(num)

print(square_root1(37))  # 6.082762530298219
print()

#3
import math as m

print(m.sqrt(37))  # 6.082762530298219