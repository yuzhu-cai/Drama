
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ 
    Filter the given list of any Python values to return only integers.

    Parameters:
    values (List[Any]): A list containing various Python values.

    Returns:
    List[int]: A list containing only the integer values from the input list.

    Examples:
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    >>> filter_integers([None, True, 42, 'string', 0, -1])
    [42, 0, -1]
    >>> filter_integers([3.5, 2.0, '4', 5, 6])
    [5, 6]
    >>> filter_integers([])
    []
    """
    return [value for value in values if isinstance(value, int)]

# Example usage:
if __name__ == "__main__":
    print(filter_integers(['a', 3.14, 5]))  # Output: [5]
    print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
    print(filter_integers([None, True, 42, 'string', 0, -1]))  # Output: [42, 0, -1]
    print(filter_integers([3.5, 2.0, '4', 5, 6]))  # Output: [5, 6]
    print(filter_integers([]))  # Output: []
