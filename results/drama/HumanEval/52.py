
def below_threshold(l: list, t: int) -> bool:
    """
    Return True if all numbers in the list l are below threshold t.

    Parameters:
    l (list): A list of numbers.
    t (int): The threshold value.

    Returns:
    bool: True if all elements are less than t, False otherwise.

    Examples:
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    >>> below_threshold([], 10)
    True
    """
    # Check if the list is empty
    if not l:
        return True  # An empty list is considered to have all elements below any threshold

    # Check if all elements are below the threshold
    return all(x < t for x in l)

# Example usage
print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
print(below_threshold([], 10))               # Output: True
