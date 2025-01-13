
def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    
    Args:
        l1 (list): The first list of elements.
        l2 (list): The second list of elements.
        
    Returns:
        list: A sorted list of unique common elements.
        
    Examples:
        >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
        [1, 5, 653]
        >>> common([5, 3, 2, 8], [3, 2])
        [2, 3]
    """
    # Step 1: Convert both lists to sets to remove duplicates
    set1 = set(l1)
    set2 = set(l2)
    
    # Step 2: Find the intersection of both sets to get common elements
    common_elements = set1.intersection(set2)
    
    # Step 3: Convert the set of common elements back to a list
    common_list = list(common_elements)
    
    # Step 4: Sort the list of common elements
    common_list.sort()
    
    return common_list

# Example usage:
if __name__ == "__main__":
    print(common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]))  # Output: [1, 5, 653]
    print(common([5, 3, 2, 8], [3, 2]))  # Output: [2, 3]
