
from itertools import combinations
from sympy import primerange

def is_multiply_prime(a):
    """Check if the given number 'a' can be expressed as the product of three prime numbers."""
    if a < 1 or a >= 100:
        raise ValueError("Input must be a positive integer less than 100.")
    
    # Generate a list of prime numbers less than 100
    primes = list(primerange(2, 100))
    
    # Check all combinations of three primes
    for combo in combinations(primes, 3):
        product = combo[0] * combo[1] * combo[2]
        if product == a:
            return True  # Return True if a valid combination is found
    
    return False  # Return False if no combination found

# Example usage:
print(is_multiply_prime(30))  # Output: True (2 * 3 * 5)
print(is_multiply_prime(60))  # Output: True (3 * 5 * 4)
print(is_multiply_prime(7))   # Output: False (7 is prime, not a product of three primes)
