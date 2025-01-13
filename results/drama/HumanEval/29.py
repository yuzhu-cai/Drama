
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ 
    Filter an input list of strings to include only those that start with a given prefix.

    Parameters:
    strings (List[str]): A list of strings to filter.
    prefix (str): The prefix to filter by.

    Returns:
    List[str]: A list of strings that start with the specified prefix.

    Examples:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    >>> filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'ap')
    ['apple', 'apricot']
    >>> filter_by_prefix(['dog', 'cat', 'deer'], 'd')
    ['dog', 'deer']
    """
    return [s for s in strings if s.startswith(prefix)]

# Example usage
if __name__ == "__main__":
    # Test cases
    print(filter_by_prefix([], 'a'))  # Output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
    print(filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'ap'))  # Output: ['apple', 'apricot']
    print(filter_by_prefix(['dog', 'cat', 'deer'], 'd'))  # Output: ['dog', 'deer']
