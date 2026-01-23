# Basic Function
def greet():
    print(" Basic Function: Hello! Welcome to Python functions.\n")

greet()

# Positional Parameters
def add_numbers(a, b):
    print(f" Positional Parameters: {a} + {b} = {a + b}")

add_numbers(5, 10)
add_numbers(20, 30)

# Keyword Arguments
def introduce(name, age):
    print(f"\n Keyword Arguments: My name is {name} and I am {age} years old.")

introduce(name="Ankaj", age=36)
introduce(age=25, name="Riya")  # order doesn't matter

# Default Parameters
def greet_user(name="Guest"):
    print(f"\n Default Parameters: Hello, {name}!")

greet_user("Ankaj")
greet_user()  # uses default value

# Arbitrary Positional Arguments (*args)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    print(f"\n *args Example: Sum of {numbers} = {total}")

sum_all(5, 10, 15)
sum_all(1, 2, 3, 4, 5)

# Arbitrary Keyword Arguments (**kwargs)
def display_info(**info):
    print("\n **kwargs Example:")
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Ankaj", age=36, city="Chandigarh")
display_info(product="Laptop", price=75000)
