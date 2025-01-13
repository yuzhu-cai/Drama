
def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    this function plucks the node with the smallest even value and returns it.
    The plucked node is returned in a list, [smallest_value, its index].
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4, 2, 3]
        Output: [2, 1]

    Example 2:
        Input: [1, 2, 3]
        Output: [2, 1]

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
    """
    smallest_even = float('inf')  # Initialize to infinity
    index_of_smallest_even = -1  # Initialize index to -1 (not found)

    for index, value in enumerate(arr):
        if value % 2 == 0:  # Check if the value is even
            if value < smallest_even:  # Check if it's the smallest even found
                smallest_even = value
                index_of_smallest_even = index

    if index_of_smallest_even == -1:  # No even number found
        return []
    else:
        return [smallest_even, index_of_smallest_even]

# Example usage:
print(pluck([4, 2, 3]))          # Output: [2, 1]
print(pluck([1, 2, 3]))          # Output: [2, 1]
print(pluck([]))                 # Output: []
print(pluck([5, 0, 3, 0, 4, 2])) # Output: [0, 1]
