
def median(l: list):
    """Return the median of elements in the list l.

    The median is the middle value of a sorted list. If the list has an odd number of elements,
    the median is the middle element. If the list has an even number of elements, the median
    is the average of the two middle elements.

    Args:
        l (list): A list of numerical values.

    Returns:
        float: The median of the list.

    Examples:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
        >>> median([1, 2, 3, 4])
        2.5
        >>> median([1])
        1
    """
    # Sort the list
    sorted_list = sorted(l)
    
    # Calculate the length of the list
    n = len(sorted_list)
    
    # Check if the length is odd or even
    if n % 2 == 1:  # Odd length
        return sorted_list[n // 2]
    else:  # Even length
        mid1 = sorted_list[n // 2 - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2

# Example usage:
if __name__ == "__main__":
    print(median([3, 1, 2, 4, 5]))  # Output: 3
    print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
    print(median([1, 2, 3, 4]))  # Output: 2.5
    print(median([1]))  # Output: 1
