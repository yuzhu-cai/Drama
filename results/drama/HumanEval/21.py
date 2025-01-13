
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    Args:
        numbers (List[float]): A list of float numbers to be rescaled.
        
    Returns:
        List[float]: A new list of rescaled numbers.
        
    Raises:
        ValueError: If the input list has fewer than two elements.
    
    Examples:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two elements.")

    min_value = min(numbers)
    max_value = max(numbers)

    # Avoid division by zero if all numbers are the same
    if min_value == max_value:
        return [0.0] * len(numbers)  # or return [1.0] * len(numbers) based on your preference

    rescaled = [(x - min_value) / (max_value - min_value) for x in numbers]
    return rescaled

# Example usage:
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    rescaled_numbers = rescale_to_unit(numbers)
    print(rescaled_numbers)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
