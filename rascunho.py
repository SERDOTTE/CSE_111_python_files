# practing and testing
import requests
from bs4 import BeautifulSoup
import math
from datetime import datetime

print("****************************************************")
print("This program calculates and reports the tire volume.")
print("****************************************************")
print("")

current_date_and_time = datetime.now(tz=None)
formatted_date = current_date_and_time.strftime("%Y-%m-%d")
print(formatted_date)


while True:
    width = int(input("Enter the width of the tire in mm (ex 205): "))
    ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    user_tire_dates = [width, ratio, diameter]
    
    # Concatenando os dados para formar a URL de pesquisa
    search_url = f"https://www.gpneus.com/pneus/?search={width} {ratio} {diameter}"
    
    # Enviando a solicitação HTTP para a URL de pesquisa
    response = requests.get(search_url)
    
    if response.status_code == 200:
        # Analisando o conteúdo HTML da página
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Encontrando o elemento que contém o preço
        price_element = soup.find("span", class_="price")
        
        if price_element:
            price_text = price_element.get_text(strip=True)
            price_tire = float(price_text.replace("R$", "").replace(",", "."))
            
            print(f"The price for the tire is {price_tire:.2f} BRL")
        else:
            print("Price not found on the website.")
    else:
        print("Failed to retrieve data from the website.")
    
    repeat = input("Do you want to calculate another tire volume? (yes/no): ")
    if repeat.lower() != "yes":
        break
