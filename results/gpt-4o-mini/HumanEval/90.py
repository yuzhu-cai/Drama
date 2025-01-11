
def next_smallest(lst):
    """
    Returns the 2nd smallest element of the list.
    Returns None if there is no such element.
    """
    # Remove duplicates by converting to a set
    unique_elements = set(lst)
    
    # If there are less than 2 unique elements, return None
    if len(unique_elements) < 2:
        return None
    
    # Sort the unique elements
    sorted_elements = sorted(unique_elements)
    
    # Return the second smallest element
    return sorted_elements[1]

# Test cases
print(next_smallest([1, 2, 3, 4, 5]))  # Output: 2
print(next_smallest([5, 1, 4, 3, 2]))  # Output: 2
print(next_smallest([]))                 # Output: None
print(next_smallest([1, 1]))             # Output: None
