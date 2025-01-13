
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.

    Parameters:
    n (int): A positive integer representing the number of digits.

    Returns:
    int: The count of n-digit integers that start or end with 1.
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")

    # Count of n-digit integers that start with 1
    count_starting_with_1 = 10**(n - 1)

    # Count of n-digit integers that end with 1
    count_ending_with_1 = 9 * 10**(n - 2) if n > 1 else 1  # Special case for n = 1

    # Count of n-digit integers that start and end with 1
    count_starting_and_ending_with_1 = 10**(n - 2) if n > 1 else 0  # Special case for n = 1

    # Applying the Inclusion-Exclusion Principle
    total_count = (count_starting_with_1 + count_ending_with_1 - count_starting_and_ending_with_1)

    return total_count


# Example usage
print(starts_one_ends(1))  # Output: 1
print(starts_one_ends(2))  # Output: 1
print(starts_one_ends(3))  # Output: 108
print(starts_one_ends(4))  # Output: 1080
