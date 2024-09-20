print('Welcome to the word guessing game!')
print()

magic_word = 'mosiah'
guess_word = str(input('What is your guess? ')).lower()
acount = 0

while magic_word != guess_word:
    print('\033[0;31mYour guess was not correct.\033[m')
    guess_word = str(input('What is your guess? ')).lower()
    acount = acount + 1


acount = acount + 1
print('\033[93mCongratulations! You guessed it!')
print(f'It took you {acount} guesses.\033[m')
print()
