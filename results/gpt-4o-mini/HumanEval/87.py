
def get_row(lst, x):
    coordinates = []
    
    # Iterate through each row and its index
    for row_index, row in enumerate(lst):
        # Iterate through each element in the row and its index
        for col_index, value in enumerate(row):
            # Check if the current value matches x
            if value == x:
                # Append the coordinate (row_index, col_index) to the list
                coordinates.append((row_index, col_index))
    
    # Sort the coordinates by row (ascending) and then by column (descending)
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
