
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """Out of a list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    >>> longest([])
    None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    >>> longest(['apple', 'banana', 'kiwi', 'strawberry', 'pear'])
    'strawberry'
    """
    if not strings:  # Check if the list is empty
        return None

    longest_string = strings[0]  # Initialize with the first string

    for string in strings:  # Iterate through the list of strings
        if len(string) > len(longest_string):  # Compare lengths
            longest_string = string  # Update longest string

    return longest_string  # Return the longest string found

# Example usage
if __name__ == "__main__":
    print(longest([]))  # Output: None
    print(longest(['a', 'b', 'c']))  # Output: 'a'
    print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
    print(longest(['apple', 'banana', 'kiwi', 'strawberry', 'pear']))  # Output: 'strawberry'
