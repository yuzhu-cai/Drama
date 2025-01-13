
def move_one_ball(arr):
    """Determine if the array can be sorted in non-decreasing order by performing right shift operations."""
    
    # Handle the edge case of an empty array
    if not arr:
        return True

    n = len(arr)
    sorted_arr = sorted(arr)  # Create a sorted version of the array

    # Check all possible right shifts
    for shift in range(n):
        # Create the right shifted version of the array
        shifted_arr = arr[-shift:] + arr[:-shift]
        if shifted_arr == sorted_arr:
            return True

    return False

# Example usage:
print(move_one_ball([3, 4, 5, 1, 2]))  # Output: True
print(move_one_ball([3, 5, 4, 1, 2]))  # Output: False
print(move_one_ball([]))                # Output: True
