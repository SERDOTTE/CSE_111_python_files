selected_year = int(input("Enter the year of interest: "))

overall_min_life = 9999
overall_min_country = ""
overall_min_year = 0
overall_max_life = 0
overlall_max_year = 0
overall_max_country = ""

with open("life-expectancy.csv") as country_files:
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
    
    print(f"The overall max life expectancy is: {overall_max_life} from {overall_max_country} in {overlall_max_year}")
    print(f"The overall min life expectancy is: {overall_min_life} from {overall_min_country} in {overall_min_year}")
