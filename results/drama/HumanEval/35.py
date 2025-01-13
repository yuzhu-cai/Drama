
def max_element(l: list) -> int:
    """Return the maximum element in the list.

    Args:
        l (list): A list of numbers.

    Returns:
        int: The maximum element in the list. Returns None if the list is empty.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
        >>> max_element([])
        None
    """
    if not l:  # Check if the list is empty
        return None  # Return None if the list is empty

    max_val = l[0]  # Initialize max_val with the first element
    for element in l:  # Iterate through each element in the list
        if element > max_val:  # Compare each element with max_val
            max_val = element  # Update max_val if a larger element is found
    return max_val  # Return the maximum value found

# Example usage
if __name__ == "__main__":
    print(max_element([1, 2, 3]))  # Output: 3
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
    print(max_element([]))  # Output: None
