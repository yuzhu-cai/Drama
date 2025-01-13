
def unique(l: list):
    """Return sorted unique elements in a list.
    
    Args:
        l (list): A list of elements (can contain duplicates).
    
    Returns:
        list: A sorted list of unique elements.
    
    Examples:
        >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [0, 2, 3, 5, 9, 123]
    """
    # Step 1: Convert the list to a set to remove duplicates
    unique_elements = set(l)
    
    # Step 2: Convert the set back to a list
    unique_list = list(unique_elements)
    
    # Step 3: Sort the list
    sorted_list = sorted(unique_list)
    
    return sorted_list

# Example usage
if __name__ == "__main__":
    print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [0, 2, 3, 5, 9, 123]
