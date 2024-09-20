import math


# Activity 1

# def display_regular(message):
#     print(message)

# def display_uppercase(message):
#     # This could be done on one line, without creating a new variable new_message
#     new_message = message.upper()
#     print(new_message)

# def display_lowercase(message):
#     new_message = message.lower()
#     print(new_message)
    
# user_message = input("What is your message?")
# display_regular(user_message)
# display_uppercase(user_message)
# display_lowercase(user_message)

# ***************  Activity 2  *****************

def compute_area_square(side):
        return side * side
   
def compute_area_rectangle(length, width):
        return length * width
    
def compute_area_circle(radius):
        return math.pi * radius * radius
    
shape = ""

while shape != "quit":
    shape = input("What shape do you have? \nIf you want exit, enter quit.")
    shape = shape.lower()
        
    if shape == "square":
        side = float(input("\nWhat is the length of the side? "))
        area = compute_area_square(side)
        print(f"The area is {area}\n")
    
    elif shape == "rectangle":
        side = float(input("\nWhat is the length? "))
        width = float(input("What is the width? "))    
        area = compute_area_rectangle(side, width)
        print(f"The area is {area}.\n")
        
    elif shape == "circle": 
        radius = float(input("\nWhat is the radius? "))
        area = compute_area_circle(radius)
        print(f"The area is {area:.2f}.\n")
    else:
        print("Enter just only one of this shapes: saquare, rectangle or circle.\n")