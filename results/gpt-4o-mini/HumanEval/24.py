
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n.
    
    >>> largest_divisor(15)
    5
    >>> largest_divisor(28)
    14
    >>> largest_divisor(1)
    0
    >>> largest_divisor(10)
    5
    """
    if n <= 1:
        return 0  # If n is 1 or less, there are no divisors smaller than n.
    
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i

# Example usage
print(largest_divisor(15))  # Output: 5
