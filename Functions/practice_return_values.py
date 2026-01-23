# Task: Return sum, difference, and product of two numbers
def calculate(a, b):
    sum_ = a + b
    diff = a - b
    prod = a * b
    return sum_, diff, prod

s, d, p = calculate(10, 5)
print("Sum:", s)
print("Difference:", d)
print("Product:", p)

# Try with different numbers
s, d, p = calculate(7, 3)
print("Sum:", s, "Difference:", d, "Product:", p)
