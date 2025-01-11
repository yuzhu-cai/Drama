
def fibfib(n: int) -> int:
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    
    Args:
    n (int): The index of the FibFib number to compute.
    
    Returns:
    int: The n-th FibFib number.
    
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Initialize the first three FibFib numbers
    fibfib_numbers = [0, 0, 1]
    
    # Compute the FibFib numbers iteratively
    for i in range(3, n + 1):
        next_fibfib = fibfib_numbers[i - 1] + fibfib_numbers[i - 2] + fibfib_numbers[i - 3]
        fibfib_numbers.append(next_fibfib)
    
    return fibfib_numbers[n]

# Example usage
if __name__ == "__main__":
    print(fibfib(1))  # Output: 0
    print(fibfib(5))  # Output: 4
    print(fibfib(8))  # Output: 24
