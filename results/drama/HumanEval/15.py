
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.
    
    Parameters:
    n (int): The upper limit of the sequence (inclusive).
    
    Returns:
    str: A space-delimited string of numbers from 0 to n.
    
    Examples:
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # Handle the case when n is negative
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Generate the list of numbers from 0 to n
    numbers = list(range(n + 1))
    
    # Convert the list of numbers to a space-delimited string
    space_delimited_string = ' '.join(map(str, numbers))
    
    return space_delimited_string

# Example usage:
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
