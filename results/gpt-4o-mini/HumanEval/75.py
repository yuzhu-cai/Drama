
from itertools import combinations
from sympy import isprime

def generate_primes(limit):
    """Generate a list of prime numbers less than the given limit."""
    primes = []
    for num in range(2, limit):
        if isprime(num):
            primes.append(num)
    return primes

def is_multiply_prime(a):
    """Check if the given number is the multiplication of 3 prime numbers."""
    if a < 1:
        return False  # No positive product can be formed with primes if a is less than 1
    
    primes = generate_primes(100)
    
    # Check combinations of 3 primes
    for combo in combinations(primes, 3):
        if combo[0] * combo[1] * combo[2] == a:
            return True
            
    return False

# Example usage
print(is_multiply_prime(30))  # Output: True
print(is_multiply_prime(60))  # Output: True (2 * 3 * 10, but 10 is not prime)
print(is_multiply_prime(15))  # Output: False
