# file name: all_in_one_advanced_practice.py

print("===== Return Values Practice =====")

def calculate(a, b):
    """Return sum, difference, product, and division of two numbers"""
    if b != 0:
        div = a / b
    else:
        div = "Cannot divide by zero"
    return a+b, a-b, a*b, div

s, d, p, div = calculate(10, 5)
print("Sum:", s)
print("Difference:", d)
print("Product:", p)
print("Division:", div)

s, d, p, div = calculate(7, 0)
print("Sum:", s, "Difference:", d, "Product:", p, "Division:", div)
print("-"*50)

print("===== Lambda Functions Practice =====")

# Lambda to add two numbers
add = lambda x, y: x + y
print("Add 8 + 12 =", add(8, 12))

# Lambda with map to square list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared List:", squared)

# Lambda with filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)
print("-"*50)

print("===== Scope Practice =====")

x = 50  # Global

def local_scope():
    x = 10  # Local
    print("Local x inside function:", x)

def global_scope():
    global x
    x = 100  # Modify global variable
    print("Global x modified inside function:", x)

def nonlocal_scope():
    y = 20
    def inner():
        nonlocal y
        y += 15
        print("Inner y (nonlocal):", y)
    inner()
    print("Outer y after inner:", y)

local_scope()
print("Global x outside function:", x)
global_scope()
print("Global x outside function:", x)
nonlocal_scope()
print("-"*50)

print("===== Docstrings Practice =====")

def divide(a, b):
    """
    Divide two numbers.

    Parameters:
    a (int or float): numerator
    b (int or float): denominator

    Returns:
    float or str: division result, error if denominator is zero
    """
    if b == 0:
        return "Cannot divide by zero"
    return a / b

result1 = divide(10, 2)
result2 = divide(5, 0)
print("10 / 2 =", result1)
print("5 / 0 =", result2)

print("\nDocstring of divide function:")
print(divide.__doc__)
