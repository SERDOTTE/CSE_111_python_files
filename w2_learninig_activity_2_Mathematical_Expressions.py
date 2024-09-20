def temperature_farenheit_number():
    while True:
        try:
            temperature_farenheit = float(input("What is the temperature in Fahrenheit? "))
            return temperature_farenheit
        except ValueError:
            print('Please enter a valid number.')
            print()
print()

temperature_farenheit = temperature_farenheit_number()
temperature_celsius = (temperature_farenheit - 32) * 5 / 9

print(f"The temperature in Celsius is {temperature_celsius:.1f} degrees.")
print()