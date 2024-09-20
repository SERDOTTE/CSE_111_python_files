first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))

if first_number > second_number:
    print('The first number is greater.')
    print('The numbers are not equal.')
    print('The secon number is not greater.')
elif first_number == second_number:
    print('The first number is not greater.')
    print('The numbers are equal.')
    print('The secon number is not greater.')
else:
    print('The first number is not greater.')
    print('The numbers are not equal.')
    print('The second number is greater.')
    
print()

favorite_animal = input('What is your favorite animal? ')
if favorite_animal.lower() == 'dog':
    print('That´s my favorite animal too!')
else:
    print('That one is not my favorite.')