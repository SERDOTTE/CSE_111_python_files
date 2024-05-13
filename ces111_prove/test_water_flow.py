#Rodrigo Serdotte Freitas
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, pressure_loss_from_pipe_reduction, reynolds_number

def test_water_column_height():
    """
    Test function for water_column_height.
    """
    test_cases = [
        (0.0, 0.0, 0.0),   
        (0.0, 10.0, 7.5),  
        (25.0, 0.0, 25.0),  
        (48.3, 12.8, 57.9),    
    ]

    for tower_height, tank_height, expected_water_column_height in test_cases:
        water_height = water_column_height(tower_height, tank_height)
        assert water_height == pytest.approx(expected_water_column_height, abs=0.1)

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
    
def test_pressure_gain_from_water_height():
    """
    Test function for pressure_gain_from_water_height.
    """
    test_cases = [
        (0.0, 0.000),    # Water Height: 0.0 meters, Expected Pressure: 0.000 kilopascals
        (30.2, 295.628),   # Water Height: 30.2 meters, Expected Pressure: 295.628 kilopascals
        (50.0, 489.450),   # Water Height: 50.0 meters, Expected Pressure: 489.450 kilopascals
    ]

    for water_height, expected_pressure in test_cases:
        pressure = pressure_gain_from_water_height(water_height)
        assert pressure == pytest.approx(expected_pressure, abs=0.001)
                

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
    

def test_pressure_loss_from_pipe():
    """
    Test function for pressure_loss_from_pipe.
    """
    # Test cases with different parameters
    test_cases = [
        (0.048692, 0.00, 0.018, 1.75, 998.2, 0.000),   #PipeDiameter, Pipe Length, Friction Factor, Water Velocity, Water Density, Expected Pressure Loss
        (0.048692, 200.0, 0.00, 1.75, 998.2, 0.000), 
        (0.048692, 200.0, 0.018, 0.00, 998.2, 0.000),
        (0.048692, 200.00,	0.018, 1.75, 998.2, -113.008),
        (0.048692, 200.00, 0.018, 1.65, 998.2, -100.462),
        (0.286870, 1000.00, 0.013, 1.65, 998.2, -61.576),
        (0.286870, 1800.75, 0.013, 1.65, 998.2, -110.884)
                  
    ]

    # Iterate through the test cases
    for pipe_diameter, pipe_length, friction_factor, water_velocity, water_density, expected_loss  in test_cases:
        loss = pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, water_velocity, water_density)
        assert loss == pytest.approx(expected_loss, abs=0.001)

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
    
    
def test_pressure_loss_from_fittings():
    """
    Test function for pressure_loss_from_fittings.
    """
    # Test cases with different parameters
    test_cases = [
        (0.00, 3, 0.00),  # Fluid Velocity, Quantity of Fittings, Expected Pressure Loss
        (1.65, 0, 0.00),  
        (1.65, 2, -0.109),
        (1.75, 2, -0.122),
        (1.75, 5, -0.306),
    ]

    # Iterate through the test cases
    for fluid_velocity, quantity_fittings, expected_loss in test_cases:
        loss = pressure_loss_from_fittings(fluid_velocity, quantity_fittings)
        assert loss == pytest.approx(expected_loss, abs=0.001)

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
    
def test_reynolds_number():
    """
    Test function for reynolds_number.
    """
    # Test cases with different parameters
    test_cases = [
        (0.048692, 0.00, 0),   # Hydraulic Diameter, Fluid Velocity, Expected Reynolds Number
        (0.048692, 1.65, 80069),  
        (0.048692, 1.75, 84922),
        (0.286870, 1.65, 471729),
        (0.286870, 1.75, 500318),
    ]

    # Iterate through the test cases
    for hydraulic_diameter, fluid_velocity, expected_reynolds_number in test_cases:
        reynolds = reynolds_number(hydraulic_diameter, fluid_velocity)
        assert reynolds == pytest.approx(expected_reynolds_number, abs=1)

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])
    
def test_pressure_loss_from_pipe_reduction():
    """
    Test function for pressure_loss_from_pipe_reduction.
    """
    # Test cases with different parameters
    test_cases = [
        (0.28687, 0.00, 1, 0.048692, 998.2, 0.000),   # Larger Diameter, Fluid Velocity, Reynolds Number, Smaller Diameter, Expected Pressure Loss
        (0.28687, 1.65, 471729, 0.048692, 998.2, -163.744),                              
        (0.28687, 1.75, 500318, 0.048692, 998.2, -184.182),    
       
    ]

    # Iterate through the test cases
    for larger_diameter, fluid_velocity, reynolds_number_val, smaller_diameter, water_density, expected_loss in test_cases:
        # Calculate the Reynolds number for the test case
        reynolds_number_val = reynolds_number(smaller_diameter, fluid_velocity)

        # Calculate the pressure loss using the function being tested
        loss = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number_val, smaller_diameter, water_density)

        # Assert that the calculated loss is approximately equal to the expected loss
        assert loss == pytest.approx(expected_loss, abs=1.0)

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", __file__])    