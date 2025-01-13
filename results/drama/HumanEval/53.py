
def add(x: int, y: int) -> int:
    """Add two numbers x and y.

    This function takes two integers as input and returns their sum.

    Parameters:
    x (int): The first integer to be added.
    y (int): The second integer to be added.

    Returns:
    int: The sum of x and y.

    Examples:
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return x + y


result1 = add(2, 3)
print(result1)  # Output: 5

result2 = add(5, 7)
print(result2)  # Output: 12

result3 = add(-1, 1)
print(result3)  # Output: 0

result4 = add(0, 0)
print(result4)  # Output: 0
