
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in the given list of numbers, any two numbers are closer to each other than
    the given threshold.

    Parameters:
    numbers (List[float]): A list of floating-point numbers to check.
    threshold (float): The threshold for determining if two numbers are close.

    Returns:
    bool: True if there are close elements, False otherwise.

    Examples:
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):  # Compare each pair only once
            if abs(numbers[i] - numbers[j]) < threshold:
                return True  # Found a pair that is close
    return False  # No pairs found that are close

# Example usage
if __name__ == "__main__":
    print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False
    print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True
