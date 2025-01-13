
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    >>> closest_integer("3.6")
    4
    >>> closest_integer("-2.3")
    -2
    >>> closest_integer("abc")
    'Invalid input: Please provide a valid number as a string.'
    '''

    try:
        # Convert the string to a float
        num = float(value)
        
        # Get the integer part and the fractional part
        integer_part = int(num)
        fractional_part = abs(num - integer_part)
        
        # Determine rounding behavior
        if fractional_part == 0.5:
            # Round away from zero
            return integer_part + 1 if num > 0 else integer_part - 1
        else:
            # Use the built-in round for other cases
            return round(num)
    
    except ValueError:
        # Handle invalid input
        return "Invalid input: Please provide a valid number as a string."

# Example usage:
print(closest_integer("10"))      # Output: 10
print(closest_integer("15.3"))    # Output: 15
print(closest_integer("14.5"))    # Output: 15
print(closest_integer("-14.5"))   # Output: -15
print(closest_integer("3.6"))     # Output: 4
print(closest_integer("-2.3"))    # Output: -2
print(closest_integer("abc"))      # Output: Invalid input: Please provide a valid number as a string.
