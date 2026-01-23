def divide(a, b):
    """
    Divide two numbers.

    Parameters:
    a (int or float): numerator
    b (int or float): denominator

    Returns:
    float: division result
    """
    if b == 0:
        return "Cannot divide by zero"
    return a / b

result1 = divide(10, 2)
result2 = divide(5, 0)

print("10 / 2 =", result1)
print("5 / 0 =", result2)

# Print function docstring
print("\nDocstring of divide function:")
print(divide.__doc__)
