
def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string):
    """Check if the length of the string is a prime number."""
    length = len(string)
    return is_prime(length)

# Example usage:
print(prime_length('Hello'))    # True
print(prime_length('abcdcba'))  # True
print(prime_length('kittens'))   # True
print(prime_length('orange'))    # False
