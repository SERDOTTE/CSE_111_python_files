
# import emoji 
# print(emoji.emojize('ola :earth_americas:', use_aliases=True))
# print("******* exercise 01 ********")
# friends = []

# name_friend = ""
# while name_friend != "end":
#     name_friend = str(input("Type the name of a friend: "))
#     if name_friend != "end":
#         friends.append(name_friend)

# print()
# print("Your friends are: ")
# for friend in friends:
#     print(friend.capitalize())


print("******* exercise 02 ********")

# Please enter the items of the shopping list (type: quit to finish):
# Item: Milk
# Item: Bread
# Item: Candy
# Item: Carrots
# Item: quit

# The shopping list is:
# Milk
# Bread
# Candy
# Carrots

# The shopping list with indexes is:
# 0. Milk
# 1. Bread
# 2. Candy
# 3. Carrots

# Which item would you like to change? 2
# What is the new item? Apples

# The shopping list with indexes is:
# 0. Milk
# 1. Bread
# 2. Apples
# 3. Carrots

shopping_list = []

name_item = ""

print("Please enter the items of the shopping list (type: quit to finish):")
while name_item != "quit":
    name_item = str(input("Item: "))
    if name_item != "quit":
        shopping_list.append(name_item)
        
print('\nThe Shopping list is: ')
for i in range(len(shopping_list)):
    name_item = shopping_list[i]
    print(name_item)
    
    

print()
print("\nThe Shopping list with indexes is: ")
for i in range(len(shopping_list)):
    name_item = shopping_list[i]
    print(f"{i}. {name_item}")


# Remove item by user-supplied index
index_to_remove = int(input("\nWhich item would you like to change? "))
        #if 0 <= index_to_remove < len(shopping_list):
removed_item = shopping_list.pop(index_to_remove)
        #    print(f"\nItem '{removed_item}' at index {index_to_remove} has been removed from the shopping list.")
        #else:
        #    print("Invalid index provided. No item has been removed.")

# Add a user-supplied item at the position of the removed item
if index_to_remove < len(shopping_list):
    new_item = input("\nWhat is the new item? ")
    shopping_list.insert(index_to_remove, new_item)
    print(f"\nItem '{new_item}' has been added to the shopping list.")

print("\nThe updated Shopping List with indexes is: ")
for i in range(len(shopping_list)):
    name_item = shopping_list[i]
    print(f"{i}. {name_item}")
   
