
def fib4(n: int) -> int:
    """Compute the n-th element of the fib4 number sequence.
    
    The Fib4 number sequence is defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4.
    
    Args:
        n (int): The index of the desired element in the fib4 sequence.
    
    Returns:
        int: The n-th element of the fib4 sequence.
    
    Examples:
        >>> fib4(5)
        4
        >>> fib4(6)
        8
        >>> fib4(7)
        14
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize the first four elements
    fib_values = [0, 0, 2, 0]
    
    # Compute the n-th element iteratively
    for i in range(4, n + 1):
        next_value = fib_values[i - 1] + fib_values[i - 2] + fib_values[i - 3] + fib_values[i - 4]
        fib_values.append(next_value)
    
    return fib_values[n]

# Example usage
if __name__ == "__main__":
    print(fib4(5))  # Output: 4
    print(fib4(6))  # Output: 8
    print(fib4(7))  # Output: 14
