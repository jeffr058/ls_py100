# The following code raises a SyntaxError:

speed_limit = 60
current_speed = 80

if current_speed > speed_limit:                         # was missing :
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')
    
# What does a SyntaxError indicate? Try running the above code, then use the resulting error message to fix the error.

# It indicates that the interpreter doesn't understand the input (you are not speaking its language).  