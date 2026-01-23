# Calculate factorial using a function

def factorial(n):
    """Return factorial of n"""
    if n == 0 or n == 1:
        return 1
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

# Example usage
print("Factorial Examples:")
print("5! =", factorial(5))
print("0! =", factorial(0))
