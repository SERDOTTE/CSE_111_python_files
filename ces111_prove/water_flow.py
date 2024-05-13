#Rodrigo Serdotte Freitas
def water_column_height(tower_height, tank_height):
    """
    Calculate and return the height of a column of water from a tower height
    and a tank wall height.

    Parameters:
        tower_height: Height of the tower (float or int)
        tank_height: Height of the tank walls (float or int)

    Return:
        Height of the water column (float)
    """
    h = tower_height + ((3 * tank_height) / 4)
    return h

def pressure_gain_from_water_height(height):
    """
    Calculate the pressure gain from the height of a water column.

    Parameters:
        height: Height of the water column in meters (float or int)

    Return:
        Pressure in kilopascals (float)
    """
    density_water = 998.2  # kg/m^3
    gravity = 9.80665     # m/s^2

    pressure = (density_water * gravity * height) / 1000  # Pressure in kilopascals
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, water_velocity, water_density):
    """
    Calculate the pressure loss from friction within a pipe.

    Parameters:
        pipe_diameter: Diameter of the pipe in meters (float)
        pipe_length: Length of the pipe in meters (float)
        friction_factor: Friction factor of the pipe (float)
        water_velocity: Velocity of water flowing through the pipe in meters per second (float)
        water_density: Density of water in kilograms per cubic meter (float)
               
    Return:
        Pressure loss in kilopascals (float)
    """
    pressure_loss = (-(friction_factor * pipe_length * water_density * water_velocity ** 2)) / (2000 * pipe_diameter)
    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculate the pressure loss from fittings in a pipe.

    Parameters:
        fluid_velocity: Velocity of the fluid (water) in meters per second (float)
        quantity_fittings: Number of fittings in the pipe (int)

    Return:
        Pressure loss in kilopascals (float)
    """
    density_water = 998.2  # Density of water in kg/m^3
    pressure_loss = (-0.04 * density_water * (fluid_velocity ** 2) * quantity_fittings) / 2000
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculate the Reynolds number.

    Parameters:
        hydraulic_diameter: Hydraulic diameter of the pipe in meters (float)
        fluid_velocity: Velocity of the fluid (water) in meters per second (float)

    Return:
        Reynolds number (float)
    """
    density_water = 998.2  # Water density in kg/m^3
    dynamic_viscosity = 0.0010016  # Dynamic viscosity in Pascal seconds
    reynolds_number = (density_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity
    
    if reynolds_number < 1:  # Check if Reynolds number is less than 1
        reynolds_number = 1  # Set Reynolds number to 1
    return reynolds_number



def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter, water_density):
    """
    Calculate the pressure loss due to a pipe diameter reduction.

    Parameters:
        larger_diameter: Diameter of the larger pipe in meters (float)
        fluid_velocity: Velocity of the fluid (water) in meters per second (float)
        reynolds_number: Reynolds number calculated for the flow (float)
        smaller_diameter: Diameter of the smaller pipe in meters (float)
        water_density: Density of water in kg/m^3 (float)


    Return:
        Pressure loss in kilopascals (float)
    """
    water_density = 998.2  # Density of water in kg/m^3
    dynamic_viscosity = 0.0010016  # Dynamic viscosity in Pascal seconds
    
    # Check if Reynolds number is zero to avoid division by zero
    if reynolds_number == 0:
        raise ValueError("Reynolds number cannot be zero.")
    
    # Calculate the constant k
    k = (0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) - 1)

    # Calculate the pressure loss P
    pressure_loss = -(k * water_density * (fluid_velocity ** 2)) / 2000
    return pressure_loss

def convert_kpa_to_psi(pressure_kpa):
    """
    Convert pressure from kilopascals (kPa) to pounds per square inch (psi).

    Parameters:
        pressure_kpa: Pressure in kilopascals (float)

    Return:
        Pressure in pounds per square inch (float)
    """
    psi_conversion_factor = 0.145038  # Conversion factor from kPa to psi
    pressure_psi = pressure_kpa * psi_conversion_factor
    return pressure_psi

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    water_density = 998.2  # Assuming a constant value
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity, water_density)
    pressure += loss

    
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    water_density = 998.2  # Assuming a constant value
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER, water_density)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    water_density = 998.2  # Assuming a constant value
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity, water_density)
    pressure += loss

    pressure_psi = convert_kpa_to_psi(pressure)
  
    print(f"Pressure at house: {pressure_psi:.1f} pounds per square inch (psi)")
    print(f"Pressure at house: {pressure:.1f} kilopascals")


if __name__ == "__main__":
    main()

