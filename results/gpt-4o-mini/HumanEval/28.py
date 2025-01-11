
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


print(concatenate([]))          # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
