# The following code prints the numbers from 1 to 10. Modify it so that it instead prints the numbers from 10 to 1 in descending order, followed by 'Launch!'.

for i in range(10, 0, -1):
    print(i)
    if i == 1:
        print('Launch!')