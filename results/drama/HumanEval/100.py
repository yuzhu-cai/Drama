
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
    >>> make_a_pile(4)
    [4, 6, 8, 10]
    """
    # Initialize an empty list to store the number of stones in each level
    stones_per_level = []
    
    # Calculate the number of stones for each level
    for level in range(n):
        if level == 0:
            stones = n  # First level has n stones
        else:
            # Determine the next odd or even number based on the first level
            if stones_per_level[0] % 2 == 0:  # n is even
                stones = stones_per_level[-1] + 2  # Next even number
            else:  # n is odd
                stones = stones_per_level[-1] + 2  # Next odd number
        
        # Append the calculated number of stones to the list
        stones_per_level.append(stones)
    
    return stones_per_level

# Example usage:
print(make_a_pile(3))  # Output: [3, 5, 7]
print(make_a_pile(4))  # Output: [4, 6, 8, 10]
