
def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n.
    
    Args:
        n (int): The number for which to find the largest divisor.
        
    Returns:
        int: The largest divisor of n that is less than n, or None if no such divisor exists.
    
    Examples:
        >>> largest_divisor(15)
        5
        >>> largest_divisor(28)
        14
        >>> largest_divisor(1)
        None
        >>> largest_divisor(0)
        None
    """
    if n <= 1:
        return None  # No divisors for numbers less than or equal to 1

    # Iterate from n-1 down to 1 to find the largest divisor
    for i in range(n - 1, 0, -1):
        if n % i == 0:  # Check if i is a divisor of n
            return i  # Return the largest divisor found

    return None  # This line is technically unreachable due to the initial check


print(largest_divisor(15))  # Output: 5
print(largest_divisor(28))  # Output: 14
print(largest_divisor(1))   # Output: None
print(largest_divisor(0))   # Output: None
