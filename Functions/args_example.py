def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Total Sum:", total)

sum_all(5, 10, 15)
sum_all(1, 2, 3, 4, 5)