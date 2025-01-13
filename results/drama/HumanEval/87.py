
def get_row(lst, x):
    """
    Given a 2D list (nested lists) and an integer x, find occurrences of x
    and return a list of tuples representing the coordinates (row, column).
    The coordinates are sorted by row index in ascending order and by column
    index in descending order.

    Parameters:
    lst (list of lists): The 2D list to search.
    x (int): The integer to find.

    Returns:
    list of tuples: A list of coordinates where x is found.
    """
    coordinates = []

    # Iterate through the nested list
    for row_index, row in enumerate(lst):
        for col_index, value in enumerate(row):
            if value == x:
                coordinates.append((row_index, col_index))

    # Sort by row index (ascending) and then by column index (descending)
    coordinates.sort(key=lambda coord: (coord[0], -coord[1]))

    return coordinates

# Example usage:
print(get_row([
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 1, 6],
    [1, 2, 3, 4, 5, 1]
], 1))  # Output: [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

print(get_row([], 1))  # Output: []

print(get_row([[], [1], [1, 2, 3]], 3))  # Output: [(2, 2)]
