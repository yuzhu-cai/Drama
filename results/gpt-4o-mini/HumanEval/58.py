
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]
    """
    # Convert lists to sets to find unique elements
    set1 = set(l1)
    set2 = set(l2)
    
    # Find the intersection of both sets
    common_elements = set1.intersection(set2)
    
    # Convert the result to a sorted list
    return sorted(common_elements)

# Example usage
print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
print(common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]
