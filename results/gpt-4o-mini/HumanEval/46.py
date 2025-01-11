
def fib4(n: int) -> int:
    """Compute the n-th element of the Fib4 number sequence."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    
    # Initialize a list to store the values of the sequence
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 0
    fib[2] = 2
    fib[3] = 0
    
    # Fill the list using the defined recurrence relation
    for i in range(4, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2] + fib[i - 3] + fib[i - 4]
    
    return fib[n]

# Test cases
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
