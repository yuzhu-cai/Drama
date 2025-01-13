
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ 
    Filter an input list of strings to include only those that contain the given substring.

    Parameters:
    strings (List[str]): A list of strings to filter.
    substring (str): The substring to search for in each string.

    Returns:
    List[str]: A list of strings that contain the substring.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Example usage:
if __name__ == "__main__":
    # Test cases
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
    print(filter_by_substring(['hello', 'world', 'python', 'programming'], 'o'))  # Output: ['hello', 'world', 'programming']
