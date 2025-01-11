
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    # Sort the list
    sorted_lst = sorted(lst)
    result = []
    
    # Use two pointers
    left = 0
    right = len(sorted_lst) - 1
    
    # Alternate between minimum and maximum
    while left <= right:
        if left == right:  # If both pointers meet, add the last element
            result.append(sorted_lst[left])
        else:
            result.append(sorted_lst[left])  # Add minimum
            result.append(sorted_lst[right])  # Add maximum
        left += 1
        right -= 1
    
    return result


print(strange_sort_list([1, 2, 3, 4]))  # Output: [1, 4, 2, 3]
print(strange_sort_list([5, 5, 5, 5]))  # Output: [5, 5, 5, 5]
print(strange_sort_list([]))             # Output: []
