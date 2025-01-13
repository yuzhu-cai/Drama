
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:
        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:
        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:
        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    # Step 1: Sort the array in descending order
    sorted_arr = sorted(arr, reverse=True)
    
    # Step 2: Select the first k elements
    top_k_elements = sorted_arr[:k]
    
    # Step 3: Sort the selected k elements in ascending order
    sorted_top_k_elements = sorted(top_k_elements)
    
    return sorted_top_k_elements

# Example usage:
print(maximum([-3, -4, 5], 3))  # Output: [-4, -3, 5]
print(maximum([4, -4, 4], 2))    # Output: [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # Output: [2]
