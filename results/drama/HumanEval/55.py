
def fib(n: int) -> int:
    """Return the n-th Fibonacci number.
    
    The Fibonacci sequence is defined as follows:
    F(1) = 1
    F(2) = 1
    F(n) = F(n-1) + F(n-2) for n > 2

    Args:
        n (int): The position in the Fibonacci sequence (1-indexed).

    Returns:
        int: The n-th Fibonacci number.

    Examples:
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(10)
    55
    >>> fib(20)
    6765
    """
    # Handle base cases
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1 or n == 2:
        return 1
    
    # Use an iterative approach for n > 2
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Example usage
if __name__ == "__main__":
    print(fib(10))  # Output: 55
    print(fib(20))  # Output: 6765
