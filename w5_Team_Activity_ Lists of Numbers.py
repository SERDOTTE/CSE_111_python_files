
list_numbers = []
number = ""

print('Enter a list of numbers, type 0 when finished.')

while number != 0:
    number = int(input("Enter number: "))
    list_numbers.append(number)
sum_numbers = sum(list_numbers)
count_numbers = len(list_numbers)
average_numbers = sum_numbers / count_numbers
max_number = max(list_numbers)
min_number = min(list_numbers)

def find_minor_positive(list_numbers):
    minor_positive = None
    for number in list_numbers:
        if number > 0:
            if minor_positive is None or number < minor_positive:
                minor_positive = number
    return minor_positive

minor_positive = find_minor_positive(list_numbers)

sorted_numbers = sorted(list_numbers)

print(f"The sum is: {sum_numbers}")
print(f"The average is: {average_numbers}")
print(f"The largest number is: {max_number}")
print(f"The smallest positive number is: {minor_positive}")
print("The sorted list is: ")
for number in list_numbers:
    print(number)
print(f"")