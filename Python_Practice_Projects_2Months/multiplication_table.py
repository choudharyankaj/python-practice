# Print multiplication table of any number

def multiplication_table(n, upto=10):
    """Print multiplication table of n up to 'upto'"""
    for i in range(1, upto+1):
        print(f"{n} x {i} = {n*i}")

# Example usage
print("Multiplication Table of 5:")
multiplication_table(5)
