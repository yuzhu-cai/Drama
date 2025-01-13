
import math

def is_prime(n):
    """Return True if a given number is prime, and False otherwise.
    
    A prime number is a natural number greater than 1 that cannot be formed 
    by multiplying two smaller natural numbers. The only divisors of a prime 
    number are 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if n is prime, False otherwise.

    Examples:
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # Handle edge cases for numbers less than 2
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n <= 3:
        return True   # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False  # eliminate multiples of 2 and 3

    # Check for factors from 5 to sqrt(n)
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

# Example usage
if __name__ == "__main__":
    print(is_prime(6))      # Output: False
    print(is_prime(101))    # Output: True
    print(is_prime(11))     # Output: True
    print(is_prime(13441))  # Output: True
    print(is_prime(61))     # Output: True
    print(is_prime(4))      # Output: False
    print(is_prime(1))      # Output: False
