
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.
    '''
    # Check for duplicates using a set
    seen = set()
    for num in lst:
        if num in seen:
            return False  # More than one occurrence of num
        seen.add(num)
    
    # Check if the list is sorted
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False  # Not sorted in ascending order
    
    return True  # The list is sorted and has no duplicates

# Test cases
print(is_sorted([5]))  # ➞ True
print(is_sorted([1, 2, 3, 4, 5]))  # ➞ True
print(is_sorted([1, 3, 2, 4, 5]))  # ➞ False
print(is_sorted([1, 2, 3, 4, 5, 6]))  # ➞ True
print(is_sorted([1, 2, 3, 4, 5, 6, 7]))  # ➞ True
print(is_sorted([1, 3, 2, 4, 5, 6, 7]))  # ➞ False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # ➞ True
print(is_sorted([1, 2, 2, 2, 3, 4]))  # ➞ False
