
def monotonic(l: list) -> bool:
    """Return True if list elements are monotonically increasing or decreasing.
    
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    >>> monotonic([])
    True
    >>> monotonic([5])
    True
    >>> monotonic([1, 2, 2, 3])
    True
    >>> monotonic([3, 3, 2, 1])
    True
    """
    # Check if the list is empty or has one element
    if len(l) <= 1:
        return True
    
    increasing = True
    decreasing = True
    
    # Iterate through the list and compare each element with the next
    for i in range(len(l) - 1):
        if l[i] < l[i + 1]:
            decreasing = False
        elif l[i] > l[i + 1]:
            increasing = False
        
        # If both increasing and decreasing are False, we can return False
        if not increasing and not decreasing:
            return False
    
    return increasing or decreasing

# Example usage:
print(monotonic([1, 2, 4, 20]))  # Output: True
print(monotonic([1, 20, 4, 10]))  # Output: False
print(monotonic([4, 1, 0, -10]))  # Output: True
print(monotonic([]))               # Output: True
print(monotonic([5]))              # Output: True
print(monotonic([1, 2, 2, 3]))     # Output: True
print(monotonic([3, 3, 2, 1]))     # Output: True
