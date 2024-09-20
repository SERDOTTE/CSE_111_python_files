import datetime

date_current = datetime.datetime.now()  # get current date
numb_day_week = date_current.weekday()  # Get the day of the week number (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
day_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # List of weekday names

print("Today is", day_week[numb_day_week],"!") # Display the current day of the week on the screen

day_of_week = day_week[numb_day_week] 
print(day_of_week)

# Initialize variables to store information
prices = []
quantities = []

# Loop to receive user input until price is 0
while True:
    price = float(input("Enter with the price (or 0 to end): "))
    
    # If price is 0, exit the loop
    if price == 0:
        break
    
    quantity = int(input("Enter the quantity: "))
    
   # Stores price and quantity in lists
    prices.append(price)
    quantities.append(quantity)

# Calculates the sum of prices multiplied by quantities
subtotal = sum([price * quantity for price, quantity in zip(prices, quantities)])

# Print the Subtotal
print("The Subtotal purchases are: U$ {:.2f}".format(subtotal))


if subtotal >= 50 and (day_of_week == "Tuesday" or day_of_week == "Wednesday"):
    discount = subtotal * 0.10
    print("You have a discount of 10% on your subtotal.")
    print("Discount amount:", discount)
    subtotal = subtotal - discount
    
elif subtotal < 50 and (day_of_week == "Tuesday" or day_of_week == "Wednesday"): 
    addit_amount = 50 - subtotal
    print(f"With an additional U$ {addit_amount:.2f} in purchases, you will be entitled to a 10% discount.")
    
else:
   print("No discount available for today or subtotal does not meet the criteria.") 
   

print(f"Your subtotal is: U$ {subtotal:.2f}.")
tax = subtotal * 0.06
print(f"Tax is: U$ {tax:.2f}")
total_due = subtotal + tax
print(f"Total amount due is U$ {total_due:.2f}")

