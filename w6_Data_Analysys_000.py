import csv

with open("life-expectancy.csv") as data_analysis_csv:
    reader_csv = csv.reader(data_analysis_csv)


# enter values
highest_expectation = 0
lowest_expectation = 100.000
highest_expectation_user = 0
lowest_expectation_user = 100.000
average_year = 0
count = 0


# verify if the enter is valid

while True:
    user_year = input("Enter the year of interest (4 Digits): ")

    if user_year.isdigit() and len(user_year) == 4:
        user_year = int(user_year)
        break
    else:
        print("Enter a valid 4-digits year. Ex: 1985 ")

# open file
with open("life-expectancy.csv") as the_list:
    next(the_list)
    for item in the_list:

        # split list
        parts = item.split(",")

        # definy itens in list
        country = parts[0]
        year = int(parts[2])
        life = float(parts[3])

# add the years of user input
        if year == user_year:
            average_year += life
            count += 1

        # lowest expectation
        if life < lowest_expectation:
            lowest_expectation = life
            lowest_country = country
            lowest_year = year

        # highest expectation
        if life > highest_expectation:
            highest_expectation = life
            highest_country = country
            highest_year = year

        # lowest expectation of user enter
        if int(year) == user_year:
            if life < lowest_expectation_user:
                lowest_expectation_user = life
                lowest_country_user = country

            # highest expectation for user enter
            if life > highest_expectation_user:
                highest_expectation_user = life
                highest_country_user = country

                lowest_expectation_user = int(lowest_expectation_user)
                highest_expectation_user = int(highest_expectation_user)

    # verify if the year of the user enter is valid
    if count > 0:
        average_expectation = average_year / count
    else:
        average_expectation = 0


# prints
print()
print(f"The overall max life expectancy is: {highest_expectation} from {highest_country} in {highest_year}")

print(f"The overall min life expectancy is: {lowest_expectation} from {lowest_country} in {lowest_year}")

print()
print(f"For the year {user_year}: ")


if count > 0:
    print(f"The average life expectancy across all countries was {average_expectation:.2f}")

    print(f"The max life expectancy was in {highest_country_user} with {highest_expectation_user}")

    print(f"The min life expectancy was in {lowest_country_user} with {lowest_expectation_user}")
else:
    print("No data found for this year")
print()
