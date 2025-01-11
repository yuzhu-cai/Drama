
def is_prime(num: int) -> bool:
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

def prime_fib(n: int) -> int:
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
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
    fib1, fib2 = 0, 1  # Starting values for Fibonacci sequence
    count = 0  # Count of Fibonacci primes found

    while True:
        fib1, fib2 = fib2, fib1 + fib2  # Generate next Fibonacci number
        if is_prime(fib2):  # Check if it's prime
            count += 1  # Increment count of Fibonacci primes
            if count == n:  # If we've found the n-th Fibonacci prime
                return fib2  # Return it

# Example usage:
if __name__ == "__main__":
    print(prime_fib(1))  # Output: 2
    print(prime_fib(2))  # Output: 3
    print(prime_fib(3))  # Output: 5
    print(prime_fib(4))  # Output: 13
    print(prime_fib(5))  # Output: 89
