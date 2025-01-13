
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting.
    The array will be sorted in ascending order if the sum of the first and last elements is odd,
    or in descending order if the sum is even.

    Note:
    * The original array remains unchanged.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    
    # Check if the array is empty
    if not array:
        return []
    
    # Calculate the sum of the first and last elements
    first_element = array[0]
    last_element = array[-1]
    total_sum = first_element + last_element
    
    # Create a copy of the original array
    sorted_array = array.copy()
    
    # Sort the array based on the sum being odd or even
    if total_sum % 2 == 0:
        # If the sum is even, sort in descending order
        sorted_array.sort(reverse=True)
    else:
        # If the sum is odd, sort in ascending order
        sorted_array.sort()
    
    return sorted_array

# Example usage
print(sort_array([]))  # Output: []
print(sort_array([5]))  # Output: [5]
print(sort_array([2, 4, 3, 0, 1, 5]))  # Output: [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # Output: [6, 5, 4, 3, 2, 1, 0]
