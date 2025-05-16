# Building on your solutions from the previous exercises, write a function local_greet that takes a locale as input, and returns a greeting. The locale lets us greet people from different countries appropriately, even when they share a common language, for example:

# my solution
def local_greet(locale):
    def extract_language(locale):
        return locale.split('_')[0]
    
    def extract_region(locale):
        return locale.split('_')[1].split('.')[0]
    
    my_tuple = (extract_language(locale), extract_region(locale))

    match my_tuple:
        case ('en', 'US'):
            return 'Hi!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case ('fr', _):
            return 'Salut!'
        case ('pt', _):
            return 'Olá!'
        case ('de', _):
            return 'Hallo!'
        case ('sv', _):
            return 'Hej!'
        case ('af', _):
            return 'Haai!'
        case _:
            return 'Goodbye!'
# end of my solution

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

# Distinguish greetings for English speaking countries like the US, UK, Canada, or Australia in your implementation, and feel free to fall back on the language-specific greetings in all other cases, for example:

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

# When implementing local_greet, make sure you re-use your extract_language, extract_region, and greet functions from the previous exercises.

# If you're interested, you can find a list of locales here.