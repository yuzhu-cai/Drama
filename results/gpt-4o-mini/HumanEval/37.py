
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.
    
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Extract even indexed values
    even_values = [l[i] for i in range(0, len(l), 2)]
    
    # Sort the even indexed values
    even_values.sort()
    
    # Create a new list to hold the result
    result = l[:]  # Start with a copy of the original list
    
    # Replace even indexed positions with sorted values
    for i, value in enumerate(even_values):
        result[i * 2] = value  # Place sorted value at the correct even index
    
    return result

# Example usage
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
