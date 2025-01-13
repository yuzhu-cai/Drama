
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    From a given list of integers, generate a list of rolling maximum elements found until the given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum values.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:  # Check if the input list is empty
        return []

    rolling_max = []  # This will hold the rolling maximum values
    current_max = numbers[0]  # Initialize current_max with the first element

    for value in numbers:
        current_max = max(current_max, value)  # Update current_max
        rolling_max.append(current_max)  # Append the current maximum to the result list

    return rolling_max

# Example usage:
if __name__ == "__main__":
    input_data = [1, 2, 3, 2, 3, 4, 2]
    result = rolling_max(input_data)
    print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]
