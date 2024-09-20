import math

pi_value = math.pi

print()
length_square = float(input('What is the lenght of a side of the square? '))
area_square = length_square * 2
print(f'The area of the square is: {area_square: .1f}')

square_centimeter = area_square / 100
print(f'The area of the square in centimeters is: {square_centimeter:.2f}')
square_meter = area_square / 10000
print(f'The area of the square in meters is: {square_meter:.4f}')
print()


lenght_rectangle = float(input('What is the lenght of rectangle? '))
width_rectangle = float(input('What is the width of the rectangle? '))
area_rectangle = lenght_rectangle * width_rectangle
print(f'The area of the rectangle is: {area_rectangle: .1f}')
rectangle_centimeter = area_rectangle / 100
print(f'The area of the rectangle in centimeters is: {rectangle_centimeter:.2f}')
rectangle_meter = area_rectangle / 10000
print(f'The area of the rectangle in meters is: {rectangle_meter:.4f}')
print()

radius_circle = float(input('What is the radius of the circle? '))
area_circle = math.pi * radius_circle ** 2
print(f'The are a of the circle is: {area_circle: .4f}')
circle_centimeter = area_circle / 100
print(f'The area of the circle in centimeters is: {circle_centimeter:.2f}')
circle_meter = area_circle / 10000
print(f'The area of the circle in meters is: {circle_meter:.4f}')
print()

single_lenght_value = float(input('Enter a single length value: '))
single_lenght_square_area = single_lenght_value ** 2
print(f'Your square area is: {single_lenght_square_area:.2f}')


circle_single_lenght = 2 * math.pi * single_lenght_value
print(f'Your single legth circle is: {circle_single_lenght:.2f}')

cub_volume_single_lenght = single_lenght_value ** 3
print(f'Your single length cube is: {cub_volume_single_lenght:.2f}')

sphere_volume_single_lenght = (4 / 3) * math.pi * (single_lenght_value ** 3)
print(f'Your single length sphere is: {sphere_volume_single_lenght:.2f}')
print()


