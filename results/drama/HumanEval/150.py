
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    """Return x if n is a prime number, otherwise return y."""
    if is_prime(n):
        return x
    else:
        return y

# Example usage:
print(x_or_y(7, 34, 12))  # Output: 34 (since 7 is prime)
print(x_or_y(15, 8, 5))   # Output: 5 (since 15 is not prime)
