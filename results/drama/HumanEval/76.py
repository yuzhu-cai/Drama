
def is_simple_power(x, n):
    """Returns True if x is a simple power of n (i.e., n**k = x for some integer k >= 0),
    and False otherwise.
    
    Args:
    x (int): The number to check.
    n (int): The base number.
    
    Returns:
    bool: True if x is a simple power of n, False otherwise.
    """
    
    # Handle special cases
    if n == 0:
        return x == 0  # 0^k = 0 only if x is 0
    if n == 1:
        return x == 1  # 1^k = 1 only if x is 1
    if n == -1:
        return x in (1, -1)  # -1^k = 1 if k is even, -1 if k is odd

    # For n > 1 or n < -1, we check powers
    k = 0
    current_power = 1  # n^0 = 1
    while current_power < x:
        k += 1
        current_power *= n  # This is equivalent to n^k
        if current_power == x:
            return True

    return False

# Example usage
print(is_simple_power(1, 4))  # True, since 4^0 = 1
print(is_simple_power(2, 2))  # True, since 2^1 = 2
print(is_simple_power(8, 2))  # True, since 2^3 = 8
print(is_simple_power(3, 2))  # False, since no integer k satisfies 2^k = 3
print(is_simple_power(3, 1))  # False, since 1^k = 1 for any k
print(is_simple_power(5, 3))  # False, since no integer k satisfies 3^k = 5
