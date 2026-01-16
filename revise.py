# ===============================
# Python Basics – Mini Summary
# ===============================

# 1. Variables
# Declaration & assignment
x = 5
a, b = 10, 20  # multiple assignment
PI = 3.14      # constant (by convention)

# 2. Data Types
# int, float, str, bool, complex
num_int = 10
num_float = 10.5
name = "Ankaj"
flag = True
c = 1 + 2j

# 3. Type Casting
num_str = "15"
num_int_cast = int(num_str)
num_float_cast = float(num_str)

# 4. Input / Output
# Basic input and print
# Uncomment below lines to try
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello", name)
# print(f"Hello {name}, you are {age} years old.")
# print("Hello %s, you are %s years old." % (name, age))
# print("Hello {} , you are {} years old.".format(name, age))

# 5. Operators
# Arithmetic: +, -, *, /, %, //, **
# Comparison: ==, !=, >, <, >=, <=
# Logical: and, or, not
# Assignment: =, +=, -=, *=, /=
# Bitwise: &, |, ^, ~, <<, >>

# ===============================
# Practice Programs
# ===============================

# 1. Rectangle Area & Perimeter
length = float(input("Enter rectangle length: "))
breadth = float(input("Enter rectangle breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print("Rectangle Area =", area)
print("Rectangle Perimeter =", perimeter)

# 2. Circle Area & Circumference
radius = float(input("Enter circle radius: "))
pi = 3.14
circle_area = pi * radius * radius
circumference = 2 * pi * radius
print("Circle Area =", circle_area)
print("Circumference =", circumference)

# 3. Square Area & Perimeter
side = float(input("Enter square side length: "))
square_area = side * side
square_perimeter = 4 * side
print("Square Area =", square_area)
print("Square Perimeter =", square_perimeter)

# 4. Cuboid Volume
length = float(input("Enter cuboid length: "))
breadth = float(input("Enter cuboid breadth: "))
height = float(input("Enter cuboid height: "))
volume = length * breadth * height
print("Cuboid Volume =", volume)

# 5. Arithmetic Operations
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
print("Floor Division =", num1 // num2)
print("Modulus =", num1 % num2)
print("Power =", num1 ** num2)

# 6. Type Casting Practice
num = input("Enter a number (string): ")
num_int = int(num)
num_float = float(num)
print("Original string:", num)
print("Integer:", num_int)
print("Float:", num_float)
print("Integer + 5 =", num_int + 5)
print("Float + 5 =", num_float + 5)

# 7. Comparison & Logical Operators
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("num1 > num2:", num1 > num2)
print("num1 == num2:", num1 == num2)
print("num1 < num2:", num1 < num2)
print("(num1 > 10) and (num2 > 10):", (num1 > 10) and (num2 > 10))
print("(num1 < 10) or (num2 < 10):", (num1 < 10) or (num2 < 10))
print("not(num1 > num2):", not(num1 > num2))

# 8. String Formatting Practice
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello %s, you are %s years old." % (name, age))
print("Hello {}, you are {} years old.".format(name, age))
print(f"Hello {name}, you are {age} years old.")
