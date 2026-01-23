# Task: Create a function to calculate area of a rectangle
def rectangle_area(length, width):
    return length * width

# Positional arguments
print("Area (Positional):", rectangle_area(5, 10))

# Keyword arguments
print("Area (Keyword):", rectangle_area(width=7, length=3))
