# What will the following code print?

print('abc-def'.isalpha())      # False
print('abc_def'.isalpha())      # False
print('abc def'.isalpha())      # False?
print('abc def'.isalpha() and
      'abc def'.isspace())      # False
print('abc def'.isalpha() or
      'abc def'.isspace())      # False
print('abcdef'.isalpha())       # True
print('31415'.isdigit())        # True
print('-31415'.isdigit())       # False
print('31_415'.isdigit())       # False
print('3.1415'.isdigit())       # False
print(''.isspace())             # False