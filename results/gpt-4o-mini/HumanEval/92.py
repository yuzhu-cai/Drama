
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
    '''
    # Check if all inputs are integers
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        # Check if any number is equal to the sum of the other two
        return x == y + z or y == x + z or z == x + y
    return False

# Test cases
print(any_int(5, 2, 7))  # ➞ True
print(any_int(3, 2, 2))  # ➞ False
print(any_int(3, -2, 1)) # ➞ True
print(any_int(3.6, -2.2, 2)) # ➞ False
