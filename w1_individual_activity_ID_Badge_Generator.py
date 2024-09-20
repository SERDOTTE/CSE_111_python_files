import re

def first_name():
    while True:
        first = input('First name: ')
        if first.isalpha():
            return first
        else:
            print('Please enter letters only.')

def last_name():
    while True:
        last = input('Last name: ')
        if last.isalpha():
            return last
        else:
            print('Please enter letters only.')

def phone_number():
    while True:
        phone_number = input('Phone number (format: xxxxxxxxxx): ')

        digits_only = re.sub(r'\D', '', phone_number)

        # Verificamos se a entrada tem 10 dígitos
        if len(digits_only) == 10:
            # Formato desejado: (xxx) xxx-xxxx
            formatted_number = "({}) {}-{}".format(digits_only[:3], digits_only[3:6], digits_only[6:])
            return formatted_number
        else:
            print('Please enter a valid 10-digit phone number without spaces, hyphens, or parentheses.')

def id_number():
    while True:
        id_num = input('ID Number: ')
        if id_num.isdigit():
            return id_num
        else:
            print('Please enter numbers only.')

def hair_color():
    while True:
        hair = input('What is your hair color? ')
        if hair.isalpha():
            return hair
        else:
            print('Please enter letters only.')

def eyes_color():
    while True:
        eyes = input('What color are your eyes? ')
        if eyes.isalpha():
            return eyes
        else:
            print('Please enter letters only.')

def month_start():
    while True:
        month = input('What month did you start? ')
        if month.isalpha():
            return month
        else:
            print('Please enter letters only.')

def in_training():

    while True:
        training = input('Have you completed the training? Select an option (yes/no): ')
        if training == 'yes' or training == 'no':
            return training
        else:
            print('Please enter either "yes" or "no".')

print('Please enter the following information:')
first = first_name()
last = last_name()
email = input('Email address: ')
phone = phone_number()
job = input('Job title: ')
id_num = id_number()
hair = hair_color()
eyes = eyes_color()
month = month_start()
training = in_training()
column1_width = 10
formatted_output_hair_eyes = 'Hair: {:<{}} Eyes: {}'.format(hair.capitalize(), column1_width, eyes.capitalize())
formatted_output_month_training = "Month: {:<{}}Training: {}".format(month.capitalize(), column1_width, training.capitalize())

print()
print('The ID Card is: ')
print('----------------------------------------')
print('{}, {}'.format(last.upper(), first.capitalize()))
print(job.capitalize())
print('ID: {}'.format(id_num))
print()
print(email.lower())
print(phone)
print()
print(formatted_output_hair_eyes)
print(formatted_output_month_training)
print('----------------------------------------')