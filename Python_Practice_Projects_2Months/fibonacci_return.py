# Return first n Fibonacci numbers as a list

def fibonacci(n):
    """Return first n Fibonacci numbers"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

# Example usage
print("Fibonacci 10 numbers:", fibonacci(10))
