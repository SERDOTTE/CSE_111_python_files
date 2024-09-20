import random

# number = random.randint(1, 10)
# print()
# print(number)

play_again = 'Yes' 
while play_again == 'Yes':

    magic_number = random.randint(1, 100)
    guess_number = 0
    count = 0
    print(magic_number)



    while guess_number != magic_number:
        guess_number = int(input('What is your guess: '))
        count = count + 1
        print(f'Guess number {count}')    
        if guess_number > magic_number:
            print('Lower')
        elif guess_number < magic_number:
            print('Higher')
        else:
            print('You guessed it!')
            print(f'You did it after {count} guesses.')
            
    play_again = str(input('Do you want to play again? ')).capitalize()
    

