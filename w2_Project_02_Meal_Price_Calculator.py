childs_meal_price = float(input('What is the price of child´s meal? $'))
# Try to convert input to a floating point number
adults_meal_price = float(input('What is the price of adult´s meal? $'))
children_amount = int(input('How many children are there? '))
adult_amount = int(input('How many adults are there? '))

child_total = childs_meal_price * children_amount
adult_total = adults_meal_price * adult_amount


# Setting the price of drinks
water_price = 2.50
juice_price = 5.00
soda_price = 4.00

# Initializing the grand total
grand_total = 0.0

# Asking if any drinks were consumed
while True:
    consumed_drink = input("\nDo you consumed any drink? (yes/no): ").lower()

    # Cheking the answer
    if consumed_drink == "yes":
        # Showing drinks options
        print("Drinks options:")
        print("1. Water")
        print("2. Juice")
        print("3. Soda")
        print()

        # Requesting drink choice by number
        request_number = int(input("Choose the number of the consumed drink: "))

        # Checking the choice and getting the quantity
        if request_number in [1, 2, 3]:
            quantity = int(input("Quantity consumed: "))

            # Calculating the total of the chosen drink
            if request_number == 1:
                total_drink = quantity * water_price
                chosen_drink = "Water"
            elif request_number == 2:
                total_drink = quantity * juice_price
                chosen_drink = "Juice"
            elif request_number == 3:
                total_drink = quantity * soda_price
                chosen_drink = "Soda"

            # Adding to grand total
            grand_total += total_drink

            # Displaying the total of the chosen drink
            print(f"Total spent on {chosen_drink}: ${total_drink:.2f}")
        else:
            print("Invalid number. Please choose between 1, 2 ou 3.")
    else:
        break  # Exit the loop if the user no longer consumes drinks

# Displaying the grand total
print(f"\nTotal spent on drinks: ${grand_total:.2f}")



subtotal = child_total + adult_total + grand_total

print()
print(f'Subtotal: ${subtotal:.2f}')
print()

sales_tax_rate = float(input('What is the sales tax rate? '))
sales_tax = (sales_tax_rate / 100) * subtotal

print(f'Sales Tax: ${sales_tax:.2f}')
total = subtotal + sales_tax
print(f'Total: ${total:.2f}')
print()

payment_amount = float(input('What is the payment amount? $'))
change = payment_amount - total
print()
print(f'Change: ${change:.2f}')
print()
