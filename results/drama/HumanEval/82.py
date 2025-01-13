
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor, not prime
    return True  # No divisors found, it is prime

def prime_length(string):
    """Return True if the length of the string is a prime number, otherwise False."""
    length = len(string)  # Calculate the length of the input string
    return is_prime(length)  # Check if the length is prime using the helper function

# Example usage:
print(prime_length('Hello'))      # Output: True (length is 5)
print(prime_length('abcdcba'))    # Output: True (length is 7)
print(prime_length('kittens'))     # Output: True (length is 7)
print(prime_length('orange'))      # Output: False (length is 6)
