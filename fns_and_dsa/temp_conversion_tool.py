# Temperature Conversion Tool

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Implement conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
get_temperature = int(input("Enter the temperature to convert: "))

if get_temperature < -273.15:
    print("Invalid temperature. Please enter a numeric value.")
    exit()
    
temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if temperature_unit == 'C':
    converted_temp = convert_to_fahrenheit(get_temperature)
    print(f"{get_temperature}°C is {converted_temp:.2f}°F")
elif temperature_unit == 'F':
    converted_temp = convert_to_celsius(get_temperature)
    print(f"{get_temperature}°F is {converted_temp:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
