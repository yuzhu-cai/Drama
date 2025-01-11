
from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Count occurrences of each number
    counts = Counter(numbers)
    
    # Create a new list with only those numbers that occur exactly once
    result = [num for num in numbers if counts[num] == 1]
    
    return result


print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
