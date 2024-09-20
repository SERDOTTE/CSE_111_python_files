#Author: Rodrigo Serdotte Freitas

wind_speed = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

def calculate_fahrenheit(temp):
    return (1.8 * temp) + 32

def calculate_wind_chill(temperature, wind_speed):
     # creating a list with the calculation of temperature with the wind
    wind_chill_list = []
    for speed in wind_speed:
        wind_chill = 35.74 + (0.6215 * temperature) - 35.75*(speed**0.16) + 0.4275*temperature*(speed**0.16)
        wind_chill = round(wind_chill, 2)
        wind_chill_list.append(wind_chill)
    return wind_chill_list

while True:
    temperature = float(input("What is the temperature? "))
    type_of_temp = input("Fahrenheit or Celsius (F/C)? ").upper()
    print()

    if type_of_temp == "F":
        temperature_fahrenheit = temperature
    elif type_of_temp == "C":
        temperature_fahrenheit = calculate_fahrenheit(temperature)
    else:
        print("Invalid input.")
        continue

    print("Temperature (ºF):", temperature_fahrenheit)
    print()
    print("Wind Chill (ºF) for each wind speed:")
    
    wind_chill_values = calculate_wind_chill(temperature_fahrenheit, wind_speed)

    # The function zip combines these two lists so that, at each iteration of the loop, speed represents an element from the wind_speed list 
    # and wind_chill represents the corresponding element from the wind_chill_values list
    for speed, wind_chill in zip(wind_speed, wind_chill_values):
        print(f"At temperature {temperature_fahrenheit}F, and wind speed {speed} mph, the windchill is: {wind_chill}F")
    print()
    break
