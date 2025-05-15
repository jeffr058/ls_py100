# Let's generalize the function from the previous exercise. Implement a function named cite that takes two string arguments: the author of the quote and what they said. It then prints the quote, as shown below.

# My solution
def cite(author, quote):
    print(f'{author} said: "{quote}"')
# End of my solution

cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."