# Author Rodrigo Serdotte Freitas

overall_min_life = 9999
overall_min_country = ""
overall_min_year = 0
overall_max_life = 0
overlall_max_year = 0
overall_max_country = ""
highest_expectation_user = 0
lowest_expectation_user = 100.000

while True:
    selected_year = input("Enter the year of interest: ")

    # Checks if the input is an integer
    if selected_year.isdigit():
        selected_year = int(selected_year)
        
        with open("life-expectancy.csv") as country_files: # This csv file must be in the same folder where this python is located
            lines = country_files.readlines()

            for line in lines[1:]:
                parts = line.split(",")
                index2_year = int(parts[2])
                index3_age = float(parts[3])
                     
                country = parts[0]
                if index3_age < overall_min_life:
                    overall_min_life = index3_age
                    overall_min_country = country
                    overall_min_year = index2_year
                    
                elif index3_age > overall_max_life:
                    overall_max_life = index3_age
                    overall_max_country = country
                    overlall_max_year = index2_year
        
            print()
            print(f"The overall max life expectancy is: {overall_max_life} from {overall_max_country} in {overlall_max_year}")
            print(f"The overall min life expectancy is: {overall_min_life} from {overall_min_country} in {overall_min_year}\n")
            
            expec_all_countries = 0
            amount_countries = 0
            
            print(f"For the year {selected_year}:")
            
            year_found = False  # Control variable
            
            for line in lines[1:]:
                parts = line.split(",")
                index2_year = int(parts[2])
                index3_age = float(parts[3])
                country = parts[0]
                
                if selected_year == index2_year:
                    year_found = True  # Updates the control variable
                    expec_all_countries += index3_age
                    amount_countries += 1
                    expec_average = expec_all_countries / amount_countries
                               
                    # lowest expectation of the year informed by the user
                    if  index3_age < lowest_expectation_user:
                        lowest_expectation_user = index3_age
                        lowest_country_user = country
                     
                    # highest expectation of the year informed by the user          
                    if index3_age > highest_expectation_user:
                        highest_expectation_user = index3_age
                        highest_country_user = country
                        
            if year_found:
                print(f"The average life expectancy across all countries was {expec_average:.2f}")
                print(f"The max life expectancy was in {highest_country_user} with {highest_expectation_user:.2f} ")
                print(f"The min life expectancy was in {lowest_country_user} with {lowest_expectation_user:.3f}\n")
            else:
                print("The year entered is not in the database.")
                print("Enter a valid year betwen 1751 and 2019\n")
            break  # Exit the while loop when a valid year is found
    else:
        print("\nThe year entered is not in the database")
        print("Enter a valid year betwen 1751 and 2019")
