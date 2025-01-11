
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 1:
        return 0  # There are no positive integers with less than 1 digit
    
    # Count of n-digit integers that start with 1
    count_start_with_1 = 10**(n-1)
    
    # Count of n-digit integers that end with 1
    if n == 1:
        count_end_with_1 = 1  # Only the number 1
    else:
        count_end_with_1 = 9 * 10**(n-2)
    
    # Count of n-digit integers that start and end with 1
    if n == 1:
        count_both = 1  # Only the number 1
    else:
        count_both = 10**(n-2)
    
    # Applying inclusion-exclusion principle
    total_count = count_start_with_1 + count_end_with_1 - count_both
    
    return total_count

# Example usage:
print(starts_one_ends(1))  # Output: 1
print(starts_one_ends(2))  # Output: 18
print(starts_one_ends(3))  # Output: 180
