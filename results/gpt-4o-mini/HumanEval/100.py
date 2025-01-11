
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    stones = []
    current_stones = n
    
    for i in range(n):
        stones.append(current_stones)
        if n % 2 == 0:  # n is even
            current_stones += 2  # next even number
        else:  # n is odd
            current_stones += 2  # next odd number (odd numbers are also incremented by 2)
    
    return stones

# Example usage:
print(make_a_pile(3))  # Output: [3, 5, 7]
print(make_a_pile(4))  # Output: [4, 6, 8, 10]
