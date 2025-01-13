
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list `numbers`.
    
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []  # Return an empty list if 'numbers' is empty
    
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])  # Append the current number
        if i < len(numbers) - 1:  # Check if it's not the last element
            result.append(delimiter)  # Append the delimiter
    
    return result

# Testing the function with provided examples
if __name__ == "__main__":
    import doctest
    doctest.testmod()
