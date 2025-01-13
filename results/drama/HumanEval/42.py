
def incr_list(l: list) -> list:
    """Return a new list with each element incremented by 1.

    Args:
        l (list): A list of numbers.

    Returns:
        list: A new list with each element incremented by 1.

    Examples:
        >>> incr_list([1, 2, 3])
        [2, 3, 4]
        >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
        [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [x + 1 for x in l]

# Example usage
if __name__ == "__main__":
    print(incr_list([1, 2, 3]))  # Output: [2, 3, 4]
    print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
