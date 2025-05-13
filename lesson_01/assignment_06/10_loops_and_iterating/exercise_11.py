# Print all of the even numbers in the following list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

# Expected Output
# 6
# 4
# 2
# 4
# 16
# 0

def even_nums(input_list):
    index_a = 0
    while index_a < len(input_list):
        index_b = 0
        while index_b < len(my_list[index_a]):
            number = my_list[index_a][index_b]
            if number % 2 == 0:
                print(number)
            index_b += 1    
        index_a += 1

even_nums(my_list)