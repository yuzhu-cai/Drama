
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci():
    """Generator for Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number that is also prime.
    
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    prime_fibs = []
    for fib in fibonacci():
        if is_prime(fib):
            prime_fibs.append(fib)
            if len(prime_fibs) == n:
                return prime_fibs[-1]

# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
