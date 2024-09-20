#Author: Rodrigo Serdotte Freitas

temperature = float(input("What is the temperature? "))
tipe_of_temp = input("Fahrenheit or Celsius (F/C)? ")
tipe_of_temp = tipe_of_temp.upper()
print("_______________________")

temp_celsius = ""
temp_fahrenheit = ""
wind_speed = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]


def calculate_fahrenheit(temp):
    fahrenreit = (1.8 * temp) + 32
    return fahrenreit


def calculate_wind_chill(temperature, wind_speed):
    # creating a list with the calculation of temperature with the wind
    wind_chill_list = []
    for speed in wind_speed:
        wind_chill = 35.74 + (0.6215 * temperature) - 35.75*(speed**0.16) + 0.4275*temperature*(speed**0.16)
        wind_chill = round(wind_chill, 2)
        wind_chill_list.append(wind_chill)
    return wind_chill_list

if tipe_of_temp == "F":
    temp_fahrenheit = temperature
    print(temp_fahrenheit)
    
elif tipe_of_temp == "C":
    temp_fahrenheit = calculate_fahrenheit(temperature)
    temperature = temp_fahrenheit
    
else:
    print("Invalid input.")

print("Temperature (ºF):", temperature)
print("_______________________")
print("Wind Chill (ºF) for each wind speed:")
print()

temperature_fahrenheit = calculate_fahrenheit(temperature)
wind_chill_values = calculate_wind_chill(temperature, wind_speed)

# The function zip combines these two lists so that, at each iteration of the loop, speed represents an element from the wind_speed list 
# and wind_chill represents the corresponding element from the wind_chill_values list
for speed, wind_chill in zip(wind_speed, wind_chill_values):
    print(f"Wind Speed: {speed} mph, the windchill is: {wind_chill}F")
print()
    

