# Purpose: Understand nested if condition

age = 22
has_id = True

if age >= 18:
    if has_id == True:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Age not eligible")
