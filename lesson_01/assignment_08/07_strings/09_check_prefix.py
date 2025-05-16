
# Write a function that checks whether a string starts with a specific prefix.

def starts_with(string, prefix):
    return string.startswith(prefix)

# Examples
print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

# My original solution before I found out there is a startswith method:
# return string[:len(prefix)] == prefix