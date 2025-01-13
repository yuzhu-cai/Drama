
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If the list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    
    count = {}
    
    # Check if the list is empty or has one element
    if len(lst) <= 1:
        return True
    
    # Iterate through the list to check for sorting and duplicates
    for i in range(len(lst)):
        # Count occurrences of each number
        if lst[i] in count:
            count[lst[i]] += 1
        else:
            count[lst[i]] = 1
        
        # If we find a number with more than 2 occurrences, return False
        if count[lst[i]] > 2:
            return False
        
        # Check if the list is sorted
        if i > 0 and lst[i] < lst[i - 1]:
            return False
            
    return True


# Test cases
print(is_sorted([5]))  # ➞ True
print(is_sorted([1, 2, 3, 4, 5]))  # ➞ True
print(is_sorted([1, 3, 2, 4, 5]))  # ➞ False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # ➞ True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # ➞ True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # ➞ False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # ➞ True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # ➞ False
