# Return Values
def square(number):
    """Return the square of a number"""
    result = number ** 2
    return result

res1 = square(5)
res2 = square(10)
print("Return Values")
print("Square of 5:", res1)
print("Square of 10:", res2)
print("-"*50)

# Lambda Functions
print("Lambda Functions")

# Lambda to add two numbers
add = lambda a, b: a + b
print("Lambda Add 5 + 10:", add(5, 10))

# Lambda with map to square a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared List using lambda + map:", squared)

# Lambda to check even/odd
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print("5 is", check_even(5))
print("6 is", check_even(6))
print("-"*50)

# Scope: Local, Global, Nonlocal
print("Scope Examples")

x = 10  # Global variable

def local_scope():
    x = 5  # Local variable
    print("Local x inside function:", x)

def global_scope():
    global x
    x = 20  # Modify global variable
    print("Global x modified inside function:", x)

def nonlocal_scope():
    y = 10
    def inner():
        nonlocal y
        y += 5
        print("Inner y (nonlocal):", y)
    inner()
    print("Outer y after inner:", y)

local_scope()
print("Global x outside function:", x)
global_scope()
print("Global x outside function:", x)
nonlocal_scope()
print("-"*50)

# Docstrings
print("Docstrings Example")

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

result = multiply(5, 10)
print("Multiply Result:", result)
print("\nFunction Docstring:")
print(multiply.__doc__)
