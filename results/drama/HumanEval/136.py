
def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''
    
    largest_negative = None
    smallest_positive = None

    for number in lst:
        if number < 0:  # Check for negative integers
            if largest_negative is None or number > largest_negative:
                largest_negative = number
        elif number > 0:  # Check for positive integers
            if smallest_positive is None or number < smallest_positive:
                smallest_positive = number

    return (largest_negative, smallest_positive)


print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Output: (None, 1)
print(largest_smallest_integers([]))                  # Output: (None, None)
print(largest_smallest_integers([0]))                  # Output: (None, None)
print(largest_smallest_integers([-10, -5, 0, 1, 2, -1, 3]))  # Output: (-1, 1)
