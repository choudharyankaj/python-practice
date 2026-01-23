num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

greater = num1>num2
equal = num1==num2
less = num1<num2

# Logical
and_check = (num1 > 10) and (num2 > 10)
or_check = (num1 < 10) or (num2 < 10)
not_check = not(num1 > num2)

print(greater, equal, less, and_check, or_check, not_check)