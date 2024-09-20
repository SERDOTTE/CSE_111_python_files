

def main():
    start_miles = float(input("A starting odometer value in miles: "))
    ending_miles = float(input("An ending odometer value in miles: "))
    amount_gallons = float(input("An amount of fuel in gallons: "))
    
    mpg = miles_per_gallon(start_miles, ending_miles, amount_gallons)
    
    lp100k = lp100k_from_mpg(mpg)
    
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.2f} liters per 100 kilometers")
    
def miles_per_gallon(start_miles, ending_miles, amount_gallons):
    mpg = abs(ending_miles - start_miles) / amount_gallons
    return mpg
   

def lp100k_from_mpg(mpg):
    fuel_eff_km_liters = 235.215 / mpg
    return fuel_eff_km_liters

main()
    