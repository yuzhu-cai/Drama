
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    >>> flip_case('Python')
    'pYTHON'
    >>> flip_case('123abcXYZ')
    '123ABCxyz'
    >>> flip_case('')
    ''
    """
    return string.swapcase()
