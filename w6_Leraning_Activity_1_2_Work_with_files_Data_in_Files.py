# print("\nLearn Activity 1:")
# print("Working with Files")


# print("The books of Book of Mormon:\n")

# with open("books.txt") as books_files:
#     for line in books_files:
#         clean_lines = line.strip()
#         print(clean_lines)
        
        
print("\nLearn Activity 2:")
print("Data in Files")

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 9999
youngest_name = ""
print(people)

for person_line in people:
    parts = person_line.split()
    print(parts)
    
    name = parts[0]
    age = int(parts[1])
    
    
    if age < youngest_age:
        youngest_age = age
        youngest_name = name
    
print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")