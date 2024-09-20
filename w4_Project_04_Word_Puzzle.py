# Progam: CSE 110 - Introduction to Programming
# Project 04: Word Puzzle
# Author: Rodrigo Serdotte Freitas

#import colorama
#from colorama import Fore

#colorama.init(autoreset=True)

print('\033[93m******************************************')
print('   Welcome to the word guessing game!')
print('******************************************\033[m')
print()

def magic_word_underscore(magic_word):
    hidden_magic_word = ''

    for letter in magic_word:
        if letter.isalpha():
            hidden_magic_word += '_ '
        else:
            hidden_magic_word += letter

    return hidden_magic_word

magic_word = 'mosiah' # define the magic word in this variable
hidden_magic_word = magic_word_underscore(magic_word)

print(f'Your hint is: {hidden_magic_word}')
print()

count = 0

while True:
    kiked_word = input('What is your guess? ')
    print()
    count = count + 1 # perform a count of attempts, including words of different sizes than the magic word
    
    if len(kiked_word) != len(magic_word):
        print('\033[0;31mSorry, the guess must have the same number of letters as the secret word.')
        print('Try another word.\033[m')
        print()
        
        continue

    revealed_letters = ''
    
    for index, (letter_kicked, letter_magic) in enumerate(zip(kiked_word, magic_word)):
       
        if letter_kicked.lower() == letter_magic.lower():
            revealed_letters += letter_kicked.upper()
            
        elif letter_kicked.lower() in magic_word.lower():
            revealed_letters += letter_kicked.lower()
            
        else:
            revealed_letters += '_ '
            
        

    print(f'Your hint is: {revealed_letters}')
    
    
    if revealed_letters.lower() == magic_word.lower():
        print()
        print('\033[93mCongratulations! You guessed it!')
        print(f'The Magic Word is: {magic_word.upper()}')
        print()
        print(f'You did it after {count} guesses.\033[m')
        print()
        break
    else:
        print('Try again.')
        print()
