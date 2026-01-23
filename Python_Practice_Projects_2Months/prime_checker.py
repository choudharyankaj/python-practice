# Check if a number is prime

def is_prime(n):
    """Return True if n is prime, else False"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):  # Only check up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Example usage
print("Prime Number Checker Examples:")
print("7 is prime?", is_prime(7))
print("15 is prime?", is_prime(15))
