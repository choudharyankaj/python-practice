# Print numbers 1 to n with FizzBuzz rules

def fizzbuzz(n):
    """
    For numbers from 1 to n:
    - Print 'FizzBuzz' if divisible by 3 and 5
    - Print 'Fizz' if divisible by 3
    - Print 'Buzz' if divisible by 5
    - Else print the number
    """
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Example usage
print("FizzBuzz up to 15:")
fizzbuzz(15)
