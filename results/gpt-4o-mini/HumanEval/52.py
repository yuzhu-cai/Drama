
def below_threshold(l: list, t: int) -> bool:
    """Return True if all numbers in the list l are below threshold t.
    
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    return all(x < t for x in l)


print(below_threshold([1, 2, 4, 10], 100))  # Output: True
print(below_threshold([1, 20, 4, 10], 5))   # Output: False
