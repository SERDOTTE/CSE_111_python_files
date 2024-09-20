word = str(input('Chose a word: ')).lower()


favorite_letter = str(input('What is your favorite letter in this word? ')).lower()
print()

for letter in word:
    if letter == favorite_letter:
        letter = letter.upper()
    print(letter, end='')
print()

for letter in word:
    if letter == favorite_letter:
        letter = '_'
    print(letter, end='')
    
print()
print()   
word = 'RODRIGO'

for letter in word:
    print(letter)

