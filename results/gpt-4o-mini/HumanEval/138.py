
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers."""
    # Check if n is less than 8
    if n < 8:
        return False
    # Check if n is even
    if n % 2 != 0:
        return False
    # If n is even and at least 8, it can be expressed as the sum of 4 positive even numbers
    return True

# Example usage:
print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True
print(is_equal_to_sum_even(10)) # True
print(is_equal_to_sum_even(14)) # True
print(is_equal_to_sum_even(7))  # False
