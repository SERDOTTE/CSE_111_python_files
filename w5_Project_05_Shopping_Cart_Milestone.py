print('*************************************')
print('Welcome to the Shopping Cart Program!')
print('*************************************\n')

shopping_cart = []
name_item = ''
main_menu = 'Please select one of the following: \n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit'

select_menu = 0  # Initializing the variable to enter the loop

while select_menu != 5:
    print(main_menu)
    select_menu = input('Please enter an action: ')
    print()
    
    if not select_menu.isdigit():
        print('\033[0;31mPlease enter a number from 1 to 5 according to the menu.\033[m')
    elif select_menu not in ['1', '2', '3', '4', '5']:
        print('\033[0;31mPlease choose one of the numbers 1 to 5.\033[m')
    else:
        select_menu = int(select_menu)  # Converting to integer only if it is valid input

        if select_menu == 1:
            name_item = input('What item would you like to add? ')
            shopping_cart.append(name_item)
            print(f'´{name_item}´ has been added to the cart.')
            print()
        elif select_menu == 2:
            print('The contents of the shopping cart are: ')
            for item in shopping_cart:
                print(item)
            print()

print('Thank you. Goodbye\n')
