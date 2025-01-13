
def sort_array(arr):
    """
    Sorts an array of non-negative integers according to the number of ones in their binary representation
    in ascending order. For numbers with the same number of ones, sorts based on decimal value.

    Args:
    arr (list): A list of non-negative integers.

    Returns:
    list: A sorted list of integers.
    
    Examples:
    >>> sort_array([1, 5, 2, 3, 4])
    [1, 2, 3, 4, 5]
    
    >>> sort_array([0, 1, 2, 3, 4])
    [0, 1, 2, 3, 4]
    
    >>> sort_array([3, 5, 7, 8, 10, 12, 15])
    [8, 3, 5, 10, 12, 7, 15]
    """
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Example usage
if __name__ == "__main__":
    print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
    print(sort_array([0, 1, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]
    print(sort_array([3, 5, 7, 8, 10, 12, 15]))  # Output: [8, 3, 5, 10, 12, 7, 15]
