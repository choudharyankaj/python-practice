def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
    a (int or float): first number
    b (int or float): second number

    Returns:
    int or float: product of a and b
    """
    return a * b

# Using the function
result = multiply(5, 10)
print("Multiply Result:", result)

# Accessing docstring
print("\nFunction Docstring:")
print(multiply.__doc__)
