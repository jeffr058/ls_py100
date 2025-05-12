# Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop.

my_list = [6, 3, 0, 11, 20, 4, 17]

# Expected Output
# 6
# 3
# 0
# 11
# 20
# 4
# 17

#while loop
i = 0
while i < len(my_list):
    number = my_list[i]
    print(number)
    i += 1

print()

# for loop
for num in my_list:
    print(num)