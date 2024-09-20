print()
print('\033[93m*************************\033[m')
print('\033[93mGrade Calculator Program:\033[m')
print('\033[93m*************************\033[m')
print()

def get_grade_percentage():
    while True:
        try:
            grade_percentage = float(input('\033[93mEnter your grade percentage: \033[m'))
            return grade_percentage
        except ValueError:
            print('\033[0;31mPlease enter a valid number with this format: 99.99..\033[m')
            print()

percentage = get_grade_percentage()

if percentage >= 90:
   letter = 'A'
elif 80 <= percentage < 90:
    letter = 'B' 
elif 70 <= percentage < 80:
    letter = 'C'    
elif 60 <= percentage < 70:
    letter = 'D' 
else: 
    letter = 'F'   


sinal = " "

last_number = int(percentage % 10)

if last_number >= 7 and percentage >= 59:
    sinal = '+'
elif last_number < 3 and percentage >= 59:
    sinal = '-'
else:
    sinal = ' '
    


print(f'\033[93mYour letter grade is: {letter}{sinal}.\033[m')
print()

