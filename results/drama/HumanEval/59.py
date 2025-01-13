
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Initialize the largest prime factor
    largest_factor = None
    
    # Check for the number of 2s that divide n
    while n % 2 == 0:
        largest_factor = 2
        n //= 2  # Divide n by 2 until it is no longer divisible
    
    # n must be odd at this point, so we can skip even numbers
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest_factor = i  # Update largest factor
            n //= i  # Divide n by i until it is no longer divisible
    
    # If n is still greater than 2, then n itself is a prime factor
    if n > 2:
        largest_factor = n
    
    return largest_factor

# Example usage
if __name__ == "__main__":
    print(f"The largest prime factor of 13195 is {largest_prime_factor(13195)}")  # Output: 29
    print(f"The largest prime factor of 2048 is {largest_prime_factor(2048)}")    # Output: 2
