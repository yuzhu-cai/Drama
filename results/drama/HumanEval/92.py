
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns True if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns False in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    any_int(3, 2, 2) ➞ False
    any_int(3, -2, 1) ➞ True
    any_int(3.6, -2.2, 2) ➞ False
    '''
    
    # Check if all parameters are integers
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        # Check if one number is equal to the sum of the other two
        return x == y + z or y == x + z or z == x + y
    else:
        return False

# Example usage:
print(any_int(5, 2, 7))    # ➞ True
print(any_int(3, 2, 2))    # ➞ False
print(any_int(3, -2, 1))   # ➞ True
print(any_int(3.6, -2.2, 2))  # ➞ False
