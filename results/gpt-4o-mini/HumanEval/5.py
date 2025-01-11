
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:  # Don't add delimiter after the last element
            result.append(delimeter)
    
    return result

# Example usage:
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
print(intersperse([], 4))          # Output: []
