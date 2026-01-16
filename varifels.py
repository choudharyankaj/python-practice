"""
food = input("food: ")
eat = "Yes" if food == "cake" else "No"
print(eat)


food = input("food: ")
print("sweet") if food == "cake" or food == "jalebi" else print("no sweet")

"""
"""
age = int(input("age: "))
vote = ("Yes", "No") [age >= 18]
"""


age = int(input("Age: "))

if age >= 18:
    print("Yes")
else:
    print("No")
