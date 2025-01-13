
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
    Args:
        lst (list of int): A non-empty list of integers.
    
    Returns:
        int: The sum of all odd elements at even positions.
    
    Examples:
        solution([5, 8, 7, 1]) ==> 12
        solution([3, 3, 3, 3, 3]) ==> 9
        solution([30, 13, 24, 321]) ==> 0
    """
    total_sum = 0
    for i in range(0, len(lst), 2):  # Iterate over even indices (0, 2, 4, ...)
        if lst[i] % 2 != 0:  # Check if the element is odd
            total_sum += lst[i]  # Add to the sum if it's odd
    return total_sum

# Example usage:
print(solution([5, 8, 7, 1]))  # Output: 12
print(solution([3, 3, 3, 3, 3]))  # Output: 9
print(solution([30, 13, 24, 321]))  # Output: 0
