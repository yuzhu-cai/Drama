
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Step 1: Sort the list
    sorted_list = sorted(l)
    
    # Step 2: Determine the length of the list
    n = len(sorted_list)
    
    # Step 3: Calculate the median
    if n % 2 == 1:  # Odd length
        return sorted_list[n // 2]
    else:  # Even length
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2

# Example usage
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
