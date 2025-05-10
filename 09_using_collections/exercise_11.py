# Without running the following code, determine what each line should print.

print('johnson' in 'Joe Johnson')           # False
print('sen' not in 'Joe Johnson')           # True
print('Joe J' in 'Joe Johnson')             # True
print(5 in range(5))                        # False
print(5 in range(6))                        # True
print(5 not in range(5, 10))                # False
print(0 in range(10, 0, -1))                # False
print(4 in {6, 5, 4, 3, 2, 1})              # True
print({1, 2, 3} in {1, 2, 3})               # True
print({3, 2} in {1, frozenset({2, 3})})     # True