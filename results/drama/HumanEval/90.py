
def next_smallest(lst):
    """
    Returns the 2nd smallest element of the list.
    Returns None if there is no such element.
    
    :param lst: List of integers
    :return: The second smallest integer or None
    """
    # Step 1: Remove duplicates by converting the list to a set
    unique_elements = set(lst)
    
    # Step 2: Sort the unique elements
    sorted_elements = sorted(unique_elements)
    
    # Step 3: Check if there are at least two unique elements
    if len(sorted_elements) < 2:
        return None
    
    # Step 4: Return the second smallest element
    return sorted_elements[1]

# Example usage:
print(next_smallest([1, 2, 3, 4, 5]))  # Output: 2
print(next_smallest([5, 1, 4, 3, 2]))  # Output: 2
print(next_smallest([]))                 # Output: None
print(next_smallest([1, 1]))             # Output: None
