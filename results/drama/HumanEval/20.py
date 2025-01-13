
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers.")

    min_diff = float('inf')  # Start with a large value
    closest_pair = (None, None)  # To store the pair of numbers

    # Compare each pair of numbers
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])  # Calculate the absolute difference
            if diff < min_diff:  # Check if this is the smallest difference found
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])  # Update the pair

    # Return the pair in ascending order
    return tuple(sorted(closest_pair))

# Example usage
if __name__ == "__main__":
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))  # Output: (2.0, 2.2)
    print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))  # Output: (2.0, 2.0)
