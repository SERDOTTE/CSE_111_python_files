def choose_article1(accessory):
    # Converts the noun accessory to lower case for easier checking
    accessory = accessory.lower()

    # List of vowels
    vogais = ['a', 'e', 'i', 'o', 'u']

    # Checks whether the initial sound is a vowel or consonant
    if accessory and accessory[0] in vogais:
        return 'an'
    else:
        return 'a'

def choose_article2(sport):
    # Converts the noun sport to lower case for easier checking
    sport = sport.lower()

    # List of vowels
    vogais = ['a', 'e', 'i', 'o', 'u']

    # Checks whether the initial sound is a vowel or consonant
    if sport and sport[0] in vogais:
        return 'an'
    else:
        return 'a'

print('Please enter the following:')
print()

adjective_1 = input('adjective: ')
animal = input('animal: ')
verb_1 = input('verb: ')
exclamation = input('exclamation: ')
verb_2 = input('verb: ')
verb_3 = input('verb: ')
accessory = input('accessory: ')
sport = input('sport: ')

print('Your story is: ')
print()
print('The other day, I was really in trouble. It all started when I saw a very \n{} {} {} yell down the hallway.'
        '"{}!" I yelled. But all \nI could think to do was to {} over and over. Miraculously, \nthat caused it to stop, '
      'but not before it tried to {} \nright in front of my family.'.format(adjective_1.lower(), animal.lower(),
                                                                              verb_1.lower(), exclamation.capitalize(),
                                                                              verb_2.lower(), verb_3.lower()))
print('That was when we realized that the {} was wearing {} {} and training \nto participate in {} {} '
      'competition.'.format(animal.lower(), choose_article1(accessory), accessory.lower(), choose_article2(sport),
                            sport.lower()))

# The expression \n performs the line break
# The characters { } represent a place reserved for variables that are informed at the end along with their formatting
