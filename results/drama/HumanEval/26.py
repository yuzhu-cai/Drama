
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Step 1: Count occurrences of each integer
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Step 2: Create a new list with integers that occur only once
    unique_integers = [num for num in numbers if count_dict[num] == 1]

    return unique_integers

# Example usage
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
    print(remove_duplicates([4, 5, 6, 7, 4, 5, 8, 9]))  # Output: [6, 7, 8, 9]
