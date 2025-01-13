
def has_only_odd_digits(n):
    """Check if the integer n contains only odd digits."""
    for digit in str(n):
        if int(digit) % 2 == 0:  # Check if the digit is even
            return False
    return True

def unique_digits(x):
    """Given a list of positive integers x, return a sorted list of all 
    elements that have no even digits.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # Filter the list to include only numbers with odd digits
    odd_digit_numbers = [num for num in x if has_only_odd_digits(num)]
    
    # Sort the resulting list in increasing order
    odd_digit_numbers.sort()
    
    return odd_digit_numbers

# Example usage
print(unique_digits([15, 33, 1422, 1]))  # Output: [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # Output: []
