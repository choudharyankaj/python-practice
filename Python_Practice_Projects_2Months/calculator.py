# Simple calculator using functions

def add(a, b):
    """Return sum of two numbers"""
    return a + b

def subtract(a, b):
    """Return difference of two numbers"""
    return a - b

def multiply(a, b):
    """Return product of two numbers"""
    return a * b

def divide(a, b):
    """Return division of a by b, handle division by zero"""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Example usage
print("Calculator Examples:")
print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))
print("6 * 7 =", multiply(6, 7))
print("20 / 5 =", divide(20, 5))
print("10 / 0 =", divide(10, 0))
