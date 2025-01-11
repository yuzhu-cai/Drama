
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    if not array:  # Check if the array is empty
        return []
    
    first_element = array[0]
    last_element = array[-1]
    total = first_element + last_element
    
    # Create a copy of the array to sort
    sorted_array = array.copy()
    
    if total % 2 == 0:  # Even sum
        sorted_array.sort(reverse=True)  # Sort in descending order
    else:  # Odd sum
        sorted_array.sort()  # Sort in ascending order
    
    return sorted_array


print(sort_array([]))  # Output: []
print(sort_array([5]))  # Output: [5]
print(sort_array([2, 4, 3, 0, 1, 5]))  # Output: [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # Output: [6, 5, 4, 3, 2, 1, 0]
