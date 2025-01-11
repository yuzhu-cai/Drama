
def largest_smallest_integers(lst):
    largest_negative = None
    smallest_positive = None
    
    for num in lst:
        if num < 0:  # Check for negative integers
            if largest_negative is None or num > largest_negative:
                largest_negative = num
        elif num > 0:  # Check for positive integers
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num
    
    return (largest_negative, smallest_positive)

# Example usage:
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
print(largest_smallest_integers([]))                   # Output: (None, None)
print(largest_smallest_integers([0]))                  # Output: (None, None)
print(largest_smallest_integers([-1, -2, 0, 1, 2]))   # Output: (-1, 1)
