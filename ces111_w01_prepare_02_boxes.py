import math

item = int(input("Enter the number of items: "))
box = int(input("Enter the number of items per box: "))

qt_box = item / box
qt_box = math.ceil(qt_box)

print(f"For {item} items, packing {box} items in each box, you will need {qt_box} boxes.")
print(qt_box)