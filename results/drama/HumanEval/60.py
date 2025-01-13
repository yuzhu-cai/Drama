
def sum_to_n(n: int) -> int:
    """
    sum_to_n is a function that sums all integers from 1 to n.

    The function calculates the sum of all integers from 1 to n using the formula:
    sum = n * (n + 1) / 2 for n > 0.
    If n is 0, the sum is 0.
    If n is negative, the function raises a ValueError.

    Parameters:
    n (int): A non-negative integer up to which the sum is calculated.

    Returns:
    int: The sum of all integers from 1 to n.

    Raises:
    ValueError: If n is a negative integer.

    Examples:
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    >>> sum_to_n(0)
    0
    >>> sum_to_n(-5)
    Traceback (most recent call last):
        ...
    ValueError: n must be a non-negative integer
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return n * (n + 1) // 2  # Using integer division for accuracy

# Example usage:
if __name__ == "__main__":
    print(sum_to_n(30))  # Output: 465
    print(sum_to_n(100))  # Output: 5050
    print(sum_to_n(5))    # Output: 15
    print(sum_to_n(10))   # Output: 55
    print(sum_to_n(1))    # Output: 1
    print(sum_to_n(0))    # Output: 0
