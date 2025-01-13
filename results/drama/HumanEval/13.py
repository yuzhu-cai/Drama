
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return the greatest common divisor of two integers a and b.
    
    Parameters:
    a (int): First integer
    b (int): Second integer

    Returns:
    int: The greatest common divisor of a and b

    Examples:
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    >>> greatest_common_divisor(0, 5)
    5
    >>> greatest_common_divisor(5, 0)
    5
    >>> greatest_common_divisor(0, 0)
    0
    """
    if a == 0 and b == 0:
        return 0  # GCD is undefined for both numbers being zero
    elif a == 0:
        return abs(b)  # GCD(0, b) = |b|
    elif b == 0:
        return abs(a)  # GCD(a, 0) = |a|

    while b != 0:
        a, b = b, a % b
    return abs(a)

# Example usage
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))   # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
    print(greatest_common_divisor(0, 5))    # Output: 5
    print(greatest_common_divisor(5, 0))    # Output: 5
    print(greatest_common_divisor(0, 0))     # Output: 0
