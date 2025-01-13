
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as input.
    It returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    seen = set()
    
    for num in l:
        # Check if the negation of the current number exists in the set
        if -num in seen:
            return True
        # Add the current number to the set
        seen.add(num)
    
    return False

# Example usage:
if __name__ == "__main__":
    print(pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
    print(pairs_sum_to_zero([1, 3, -2, 1]))  # Output: False
    print(pairs_sum_to_zero([1, 2, 3, 7]))  # Output: False
    print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Output: True
    print(pairs_sum_to_zero([1]))  # Output: False
