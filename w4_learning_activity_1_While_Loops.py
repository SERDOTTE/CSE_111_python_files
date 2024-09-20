# Author Rodrigo Serdotte Freitas

number = int(input('Please type a positive number: '))

while number < 0:
     
    print('Sorry, that is a negative number. Please try again.')
    number = int(input('Type a positive number: '))

print(f'The number is: {number}')
print()
print()


# Other exercise part 
ask = str(input('May I have a piece of candy?  ')).capitalize()

while ask != 'Yes':
   ask = str(input('May I have a piece of candy?  ')).capitalize()

print('Thak you!!')