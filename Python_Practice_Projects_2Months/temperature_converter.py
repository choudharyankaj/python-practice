# Convert temperatures between Celsius and Fahrenheit

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit"""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius"""
    return (f - 32) * 5/9

# Example usage
print("Temperature Converter Examples:")
print("25°C =", celsius_to_fahrenheit(25), "°F")
print("77°F =", round(fahrenheit_to_celsius(77), 2), "°C")
