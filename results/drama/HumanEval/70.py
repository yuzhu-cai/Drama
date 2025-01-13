
def strange_sort_list(lst):
    '''
    Given a list of integers, return the list in a strange order.
    Strange sorting is when you start with the minimum value,
    then the maximum of the remaining integers, then the next minimum,
    and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    # Step 1: Sort the input list
    sorted_list = sorted(lst)
    
    # Step 2: Initialize an empty result list
    result = []
    
    # Step 3: Initialize pointers for minimum and maximum
    left = 0
    right = len(sorted_list) - 1
    
    # Step 4: Alternate between appending min and max
    while left <= right:
        if left == right:  # If both pointers meet, append the last element
            result.append(sorted_list[left])
            break
        result.append(sorted_list[left])  # Append the minimum
        result.append(sorted_list[right])  # Append the maximum
        left += 1
        right -= 1
    
    return result

# Example usage:
print(strange_sort_list([1, 2, 3, 4]))  # Output: [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # Output: [5, 5, 5, 5]
print(strange_sort_list([]))             # Output: []
