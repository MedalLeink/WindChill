# Windchill Calculator
# By: Nkiru Madeleine Anagha



# Function to calculate wind chill
def calculate_windchill(temp_f, wind_speed):

    """Calculate and return wind chill in Fahrenheit."""

    wind_chill = 35.74 + (0.6215 * temp_f) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp_f * (wind_speed ** 0.16))
    return wind_chill

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(temp_c):

    """Convert Celsius temperature to Fahrenheit."""
    
    return (temp_c * 9/5) + 32

# Ask the user for input
temperature = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()