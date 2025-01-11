
def pluck(arr):
    smallest_even_value = float('inf')  # Start with infinity for comparison
    smallest_index = -1  # Initialize index to -1 (indicating not found)

    for index, value in enumerate(arr):
        if value % 2 == 0:  # Check if the value is even
            if value < smallest_even_value:  # Found a smaller even value
                smallest_even_value = value
                smallest_index = index

    # Check if we found any even value
    if smallest_index == -1:
        return []  # No even values found

    return [smallest_even_value, smallest_index]  # Return the result as specified

# Example usage:
print(pluck([4, 2, 3]))  # Output: [2, 1]
print(pluck([1, 2, 3]))  # Output: [2, 1]
print(pluck([]))         # Output: []
print(pluck([5, 0, 3, 0, 4, 2]))  # Output: [0, 1]
