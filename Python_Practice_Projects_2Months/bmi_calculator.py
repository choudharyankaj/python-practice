# BMI calculation using a function

def bmi(weight, height):
    """
    Calculate BMI (Body Mass Index)
    weight in kg, height in meters
    """
    return round(weight / (height ** 2), 2)  # Round to 2 decimal places

# Example usage
print("BMI Examples:")
print("Weight: 70kg, Height: 1.75m → BMI =", bmi(70, 1.75))
print("Weight: 60kg, Height: 1.6m → BMI =", bmi(60, 1.6))
