
def strlen(string: str) -> int:
    """ Return length of given string.
    
    Args:
        string (str): The input string whose length is to be calculated.
        
    Returns:
        int: The length of the input string.
        
    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
        >>> strlen('Hello, World!')
        13
        >>> strlen('   ')  # String with spaces
        3
        >>> strlen('1234567890')  # Numeric string
        10
    """
    return len(string)

# Test cases to confirm the function returns the correct length
if __name__ == "__main__":
    print(strlen(''))  # Output: 0
    print(strlen('abc'))  # Output: 3
    print(strlen('Hello, World!'))  # Output: 13
    print(strlen('   '))  # Output: 3
    print(strlen('1234567890'))  # Output: 10
