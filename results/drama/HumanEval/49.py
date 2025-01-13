
def modp(n: int, p: int) -> int:
    """
    Return 2^n modulo p (be aware of numerics).

    Parameters:
    n (int): The exponent to which 2 is raised.
    p (int): The modulus.

    Returns:
    int: The result of 2^n modulo p.

    Examples:
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    if p <= 0:
        raise ValueError("p must be a positive integer")
    
    result = 1
    base = 2 % p  # Reduce the base modulo p initially

    while n > 0:
        if n % 2 == 1:  # If n is odd
            result = (result * base) % p
        base = (base * base) % p  # Square the base
        n //= 2  # Divide n by 2

    return result

# Example usage:
if __name__ == "__main__":
    import doctest
    doctest.testmod()
