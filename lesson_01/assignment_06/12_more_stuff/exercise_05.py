# On reflection, we've decided that we don't want to rely on using a global variable in the code we wrote in the previous example. To fix this, we're going to nest the code from the previous example into an outer function:

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter          # changed global to nonlocal
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()

# There's a bug in this code. Identify the bug, and fix it.