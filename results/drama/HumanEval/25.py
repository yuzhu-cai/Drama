
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Input number should be equal to the product of all factors.
    
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(1)
    []
    >>> factorize(0)
    []
    >>> factorize(-10)
    []
    """
    
    # Handle edge cases
    if n < 2:
        return []  # No prime factors for numbers less than 2
    
    factors = []
    
    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # n must be odd at this point, so we can skip even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors

# Example usage and testing
if __name__ == "__main__":
    print(factorize(8))    # Output: [2, 2, 2]
    print(factorize(25))   # Output: [5, 5]
    print(factorize(70))   # Output: [2, 5, 7]
    print(factorize(1))    # Output: []
    print(factorize(0))    # Output: []
    print(factorize(-10))  # Output: []
