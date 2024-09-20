# Author: Rodrigo Serdotte Freitas
# Project Shopping Cart

from itertools import zip_longest

print('\033[93m*************************************')
print('Welcome to the Shopping Cart Program!')
print('*************************************\033[m\n')

itens_prices = []
shopping_cart = []

main_menu = 'Please select one of the following: \n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit'

select_menu = 0  # Initializing the variable to enter the loop

while select_menu != 5:
    print(main_menu)
    select_menu = input('Please enter an action: ')
    print()

    if not select_menu.isdigit():
        print(
            '\033[0;31mPlease enter a number from 1 to 5 according to the menu.\033[m')
    elif select_menu not in ['1', '2', '3', '4', '5']:
        print('\033[0;31mPlease choose one of the numbers 1 to 5.\033[m')
    else:
        # Converting to integer only if it is valid input
        select_menu = int(select_menu)

        if select_menu == 1:
            name_item = input('What item would you like to add? ')
            name_item = name_item.capitalize()
            shopping_cart.append(name_item)
            price = float(input(f'What is the price of {name_item}? '))
            itens_prices.append(price)
            print(f'\'{name_item}\' has been added to the cart.')
            print()
        elif select_menu == 2:
            if not shopping_cart:  # if the user selects this menu before adding items
                print('\033[0;31mThe cart is empty.\033[m')
            else:
                print('The contents of the shopping cart are: ')
                complete_shopping_cart = zip_longest(
                    shopping_cart, itens_prices, fillvalue='N/A')
                # will combine the two iterables and if one of them is longer than the other, it will fill in the missing spaces
                # This ensures that even if the two lists are different lengths, all item and price combinations are considered.
                for index, (item, price) in enumerate(complete_shopping_cart, start=1):
                # Here, we are using a for loop to iterate over all the elements in the complete_shopping_cart iterator. 
                # The enumerate() function adds a counter (index) to each element of the iterator, starting from 1 (start=1). 
                # At each iteration, we unpack the tuple (item, price) from the iterator, where item represents the item in the cart and price represents the price of that item.
                    print(f'{index}. {item} - ${price:.2f}')
            print()
        elif select_menu == 3:
            if not shopping_cart:  # if the user selects this menu before adding items
                print('\033[0;31mThe cart is empty.\033[m')
            else:
                # helps the user to choose the item to be deleted, viewing the current list
                print('The contents of the shopping cart are: ')
                for index, item in enumerate(shopping_cart, start=1):
                    print(f'{index}. {item} - ${itens_prices[index-1]:.2f}')
                index_to_remove = int(
                    input('\nWhich item would you like to remove? '))
                if 1 <= index_to_remove <= len(shopping_cart):
                    removed_item = shopping_cart.pop(index_to_remove - 1)
                    removed_price = itens_prices.pop(index_to_remove - 1)
                    print(f'\'{removed_item}\' has been removed from the cart.')
                else:
                    print('Invalid item index.')
            print()

        elif select_menu == 4:
            if not shopping_cart:  # if the user selects this menu before adding items
                print('\033[0;31mThe cart is empty.\033[m')
                print()
            else:
                total_price = sum(itens_prices)
                print(f'\033[93mThe total price of the items in the shopping cart is $ {total_price}\033[m\n')
                print()

print('\033[93mThank you. Goodbye\033[m\n')
