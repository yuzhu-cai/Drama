
def add(lst):
    """Given a non-empty list of integers lst, this function adds the even elements that are at odd indices.

    Args:
        lst (list): A non-empty list of integers.

    Returns:
        int: The sum of even elements located at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2
        add([1, 2, 3, 4, 5, 6]) ==> 6  # Only 2 and 4 are at odd indices and even
        add([10, 15, 20, 25, 30]) ==> 20  # Only 20 is at index 2 (odd) and even
    """
    total_sum = 0  # Initialize the sum to zero
    for index in range(len(lst)):
        if index % 2 == 1:  # Check if the index is odd
            if lst[index] % 2 == 0:  # Check if the element is even
                total_sum += lst[index]  # Add the even element to the sum
    return total_sum  # Return the final sum
