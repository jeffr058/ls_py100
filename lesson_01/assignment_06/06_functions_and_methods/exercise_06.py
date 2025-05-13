# What does the following code print?

# def scream(words):
#     words = words + '!!!!'
#     return
#     print(words)

# scream('Yipeee')

First, I thought it prints Yipeee!!!!
I tried a similar function on the REPL and it printed nothing. My guess for why this is the case is that the return by itself forces a return of the value None.