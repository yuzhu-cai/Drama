
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """Calculate the Mean Absolute Deviation (MAD) for a given list of numbers.
    
    The Mean Absolute Deviation is the average absolute difference between each
    element and the mean of the dataset.
    
    MAD = average | x - x_mean |
    
    Args:
        numbers (List[float]): A list of numerical values.
        
    Returns:
        float: The Mean Absolute Deviation of the input numbers.
        
    Examples:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
        >>> mean_absolute_deviation([10, 20, 30, 40, 50])
        10.0
    """
    if not numbers:  # Handle the case of an empty list
        return 0.0  # Return 0 or raise an exception based on your requirement

    # Step 1: Calculate the mean
    mean_value = sum(numbers) / len(numbers)

    # Step 2: Calculate absolute deviations from the mean
    absolute_deviations = [abs(x - mean_value) for x in numbers]

    # Step 3: Calculate the mean of absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad

# Example usage
if __name__ == "__main__":
    example_data = [1.0, 2.0, 3.0, 4.0]
    print(f"The Mean Absolute Deviation for {example_data} is: {mean_absolute_deviation(example_data)}")
