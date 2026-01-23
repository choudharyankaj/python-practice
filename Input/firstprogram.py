# User se length aur breadth lena
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))

# Area aur Perimeter calculate karna
area = length * breadth
perimeter = 2 * (length + breadth)

# Result print karna
print("Area of rectangle =", area)
print("Perimeter of rectangle =", perimeter)

####################################################

side = float(input("Enter side length of square: "))
area = side * side
perimeter = 4 * (side + area)
print("Area of square =", area)
print("Perimeter of square =", perimeter)

####################################################

length = float(input("Enter length of cuboid: "))
breadth = float(input("Enter breadth of cuboid: "))
height = float(input("Enter height of cuboid: "))
volume = length * breadth * height
print("Volume of cuboid =", volume)