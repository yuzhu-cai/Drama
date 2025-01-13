
def can_arrange(arr):
    """
    Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1, 2, 4, 3, 5]) = 3
    can_arrange([1, 2, 3]) = -1
    """
    largest_index = -1  # Initialize to -1 to indicate no such element found

    # Iterate through the array from the second element to the last
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:  # Check if the current element is less than the previous one
            largest_index = i  # Update the largest index found

    return largest_index  # Return the largest index or -1 if none found

# Example usage
print(can_arrange([1, 2, 4, 3, 5]))  # Output: 3
print(can_arrange([1, 2, 3]))         # Output: -1
