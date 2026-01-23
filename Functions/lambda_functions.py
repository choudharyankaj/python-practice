# Lambda function to add two numbers
add = lambda a, b: a + b
print("Lambda Add 5+10:", add(5, 10))

# Lambda with map to square a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared List:", squared)

# Lambda to check even/odd
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print("5 is", check_even(5))
print("6 is", check_even(6))
