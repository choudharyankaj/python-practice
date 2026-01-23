# Validate password based on rules

import re

def validate_password(password):
    """
    Password rules:
    - Minimum 8 characters
    - At least one uppercase
    - At least one lowercase
    - At least one digit
    - At least one special character
    """
    if len(password) < 8:
        return "Password too short"
    if not re.search("[A-Z]", password):
        return "Missing uppercase letter"
    if not re.search("[a-z]", password):
        return "Missing lowercase letter"
    if not re.search("[0-9]", password):
        return "Missing digit"
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Missing special character"
    return "Password is valid"

# Example usage
print("Password Validator Examples:")
print("Abc123! →", validate_password("Abc123!"))
print("StrongPass1@ →", validate_password("StrongPass1@"))
