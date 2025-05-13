# The following code uses the randrange function from Python's random library to obtain and print a random integer within a given range. Using a while loop, it keeps running until it finds a random number that matches the last number in the range. Refactor the code so it doesn't require two different invocations of randrange.

import random

highest = 10
number = 0
# number = random.randrange(highest + 1)
# print(number)

while number != highest:
    number = random.randrange(highest + 1)
    print(number)