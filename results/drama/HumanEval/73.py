
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    n = len(arr)
    changes_needed = 0
    
    # Loop through the first half of the array
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            changes_needed += 1
            
    return changes_needed

# Example usage
print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))  # Output: 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))     # Output: 1
print(smallest_change([1, 2, 3, 2, 1]))            # Output: 0
