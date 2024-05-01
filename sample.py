# Import the sleep function from the time module, so
# that the sleep function can be used in this program.
from time import sleep

# Prompt the user to enter her name.
name = input("Hello! What is your name? ")

# Print the numbers 3, 2, 1.
for i in range(3, 0, -1):
    print(i, flush=True)
    sleep(0.5)  # Pause for 1/2 second

# Use a Python f-string to format a greeting
# for the user and then print the greeting.
print(f"Welcome to CSE 111, {name}!")

# Example 2

# The input function always returns a string.
k = input("Please enter a number: ")        # string
m = input("Please enter another number: ")  # string
n = k + m          # string plus string makes string
print(f"k: {type(k)} {k}")
print(f"m: {type(m)} {m}")
print(f"n: {type(n)} {n}")
print()

# The int and float functions convert a string to a number.
p = int(input("Please enter a number: "))          # int
q = float(input("Please enter another number: "))  # float
r = p + q                     # int plus float makes float
print(f"p: {type(p)} {p}")
print(f"q: {type(q)} {q}")
print(f"r: {type(r)} {r}")

# Example 5

# Compute the total price of a pizza.

# The base price of a large pizza is $10.95
price = 10.95

# Ask the user for the number of toppings.
number_of_toppings = int(input("How many toppings? "))

# Compute the cost of the toppings.
price_per_topping = 1.45
toppings_cost = number_of_toppings * price_per_topping

# Add the cost of the toppings to the price of the pizza.
price += toppings_cost

# Print the price for the user to see.
print(f"Price: ${price:.2f}")

# Example 7

# Get the cost of an item from the user.
cost = float(input("Please enter the cost: "))

# Determine a discount rate based on the cost.
if cost < 100:
    rate = 0.10
elif cost < 250:
    rate = 0.15
elif cost < 400:
    rate = 0.18
else:
    rate = 0.20

# Compute the discount amount
# and the discounted cost.
discount = cost * rate
cost -= discount

# Print the discounted cost for the user to see.
print(f"After the discount, you will pay {cost:.2f}")
