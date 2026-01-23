# Task 1: Add two numbers using lambda
add = lambda x, y: x + y
print("Add 8 + 12 =", add(8, 12))

# Task 2: Square all numbers in a list using lambda + map
numbers = [2, 4, 6, 8]
squared = list(map(lambda x: x**2, numbers))
print("Squared List:", squared)

# Task 3: Filter even numbers using lambda + filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)
