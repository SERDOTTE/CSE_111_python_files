import math
import pandas as pd

# Dados fornecidos
data = {
    'Name': ['#1 Picnic', '#1 Tall', '#2', '#2.5', '#3 Cylinder', '#5', '#6Z', '#8Z short', '#10', '#211', '#300', '#303'],
    'Radius (centimeters)': [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10],
    'Height (centimeters)': [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11],
    'Cost per Can (U.S. dollars)': ['$0.28', '$0.43', '$0.45', '$0.61', '$0.86', '$0.83', '$0.22', '$0.26', '$1.53', '$0.34', '$0.38', '$0.42']
}

# Criar DataFrame pandas
df = pd.DataFrame(data)

# Remover o símbolo '$' da coluna 'Cost per Can (U.S. dollars)' e converter para float
df['Cost per Can (U.S. dollars)'] = df['Cost per Can (U.S. dollars)'].str.replace('$', '').astype(float)

# Exibir DataFrame
print(df)

best_store = None
best_cost = None
max_store_eff = -1
max_cost_eff = -1

def main():
    global best_store, best_cost, max_store_eff, max_cost_eff  # Declarar as variáveis globais
    print("============================================")
    for index, row in df.iterrows():
        name = row["Name"]
        radius = row['Radius (centimeters)']
        height = row["Height (centimeters)"]
        cost = row["Cost per Can (U.S. dollars)"]
        volume = compute_volume(radius, height)
        surf_area = compute_surface_area(radius, height)
        storage_efficiency = compute_storage_efficiency(volume, surf_area)
        cost_efficiency = compute_cost_efficicency(volume, cost)
        print(f"{name} -- {storage_efficiency:.2f} -- {cost_efficiency:.2f}")
        
        if storage_efficiency > max_store_eff:
            best_store = name
            max_store_eff = storage_efficiency

        
        if cost_efficiency > max_cost_eff:
            best_cost = name
            max_cost_eff = cost_efficiency
            
    print()
    print("Best can size in storage efficiency is ", best_store)
    print("Best can size in cost efficiency is ", best_cost)


def compute_storage_efficiency(volume, surf_area):
    storage_efficiency = volume / surf_area
    return storage_efficiency

def compute_cost_efficicency(volume, cost):
    cost_efficiency = volume / cost    
    return cost_efficiency
    
def compute_volume(radius, height):
    """Compute and return the volume of a cylinder.
    """

    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder.
    """
 
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area
main()
