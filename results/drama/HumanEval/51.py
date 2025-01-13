
def remove_vowels(text):
    """
    remove_vowels is a function that takes a string and returns the string without vowels.
    
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\\nghijklm")
    'bcdf\\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    # Define a set of vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    # Use a list comprehension to filter out vowels
    result = ''.join([char for char in text if char not in vowels])
    return result

# Test cases to verify correctness
if __name__ == "__main__":
    import doctest
    doctest.testmod()
