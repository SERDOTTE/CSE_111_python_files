#CSE 111
# Name: Rodrigo Serdotte Freitas
# W01 Prove: Tire Volume


import math
from datetime import datetime

print("****************************************************")
print("Tire price consultation and order records.")
print("****************************************************")
print("")

current_date_and_time = datetime.now(tz=None)
formatted_date = current_date_and_time.strftime("%Y-%m-%d")

while True:
    
    user_tire_dates = []
      
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
           
    user_tire_dates.append(width)
    user_tire_dates.append(ratio)
    user_tire_dates.append(diameter)
    
    #print("user dates: ", user_tire_dates) - I only used this line to check the user data
    
    volume_nom1 = math.pi * (width ** 2) * ratio
    volume_nom2 = (width * ratio) + (2540 * diameter)
    volume_nom = volume_nom1 * volume_nom2

    volume = volume_nom / 10000000000
    
    with open("volumes.txt", mode="at") as volumes_file:
        volumes_file.write(f"{formatted_date}, {width}. {ratio}, {diameter}, {volume:.2f}\n")
        
    found_price = False # Variable to check if the price was found
    with open("tire_prices.txt", mode="rt") as prices_file:
        for line in prices_file:
            data = line.strip().split(",")
            if not all(data):  # Checks if all elements in the list are non-empty
                continue  
            try:
                data_as_numbers = [int(item) if i != 3 else float(item) for i, item in enumerate(data)]   # Converting to integers
            except ValueError:
                print("Error converting data to numbers:", data)
                continue
            
            #I only used these lines below in the process of building the program to check and compare the data entered by the user, 
            # how the program was transforming the data extracted from the tire_prices.txt file and how the data was coming from 
            # the tire_prices.txt file.
            #print("Comparing user dates:", user_tire_dates)
            #print("Comparing data from file:", data_as_numbers[:3])
            #print("Complete data from file:", data)
                        
            if data_as_numbers[:3] == user_tire_dates:
                tire_price_return = data_as_numbers[-1]
                #print({data_as_numbers[-1]}) - I used it to check how the variable is returning
                print(f"\033[93mThe price for this tire is: U$ {tire_price_return:.2f}\033[0m")
                found_price = True
                buy = input("Do you want to buy tires with the dimensions that you entered? (yes/no): ")
                if buy.lower() == "yes":
                    phone = int(input("What is your phone number? "))
                    with open("volumes.txt", mode="at") as volumes_file:
                        volumes_file.write(f"{formatted_date}, {width}, {ratio}, {diameter}, {volume:.2f}, {phone}\n")
                    print("\033[92mThank you! Your purchase has been recorded.\033[0m")
                else:
                    print("No purchase recorded.")
                break
                
    if not found_price:
        print("\033[91mTire prices not found for the given tire dates.\033[0m")            
        
    print("")
    print(f"The approximate volume is {volume:.2f} liters")
    print("")
    
    repeat = input("Do you want to calculate another tire volume? (yes/no): ")
    if repeat.lower() != "yes":
        break
    