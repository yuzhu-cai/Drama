
def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome.
    
    A palindrome is a string that reads the same forwards and backwards.
    
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Normalize the string by removing spaces and converting to lowercase
    normalized_text = text.replace(" ", "").lower()
    # Check if the normalized string is equal to its reverse
    return normalized_text == normalized_text[::-1]

# You can run the doctests to verify the implementation
if __name__ == "__main__":
    import doctest
    doctest.testmod()
