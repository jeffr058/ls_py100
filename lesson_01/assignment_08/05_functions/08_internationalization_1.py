# Use Python's control structures to create a function that takes an ISO 639-1 language code and returns a greeting in that language. You can take the examples below or add whatever languages you like.

# my solution
def greet(lang_code):
    # if statement version
    if lang_code == 'en':
        return 'Hi!'
    elif lang_code == 'fr':
        return 'Salut!'
    elif lang_code == 'pt':
        return 'Olá!'
    elif lang_code == 'de':
        return 'Hallo!'
    elif lang_code == 'sv':
        return 'Hej!'
    elif lang_code == 'af':
        return 'Haai!'
    else:
        return 'Goodbye!'

    # match/case statement version
    match lang_code:
        case 'en':
         return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'
        case _:
            return 'Goodbye!'

# end of my solution

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!