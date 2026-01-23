# Task: Create a function to multiply all numbers
def multiply_all(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print("Multiply all:", multiply_all(2, 3, 4))
print("Multiply all:", multiply_all(5, 10))
