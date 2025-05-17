# We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game. However, we encountered an issue, as whenever we change a value in one nested list, all nested lists are affected. Can you fix the code?

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

# Appending sub_list accesses it in memory, so any mutation by matrix or sub_list affects the other. Since matrix is appending the same sub_list three times, the change will show in all three.

# My original solution replaced the sub_list and added the nested list in via slicing:
# matrix[len(matrix):] = [["-", "-", "-"]]