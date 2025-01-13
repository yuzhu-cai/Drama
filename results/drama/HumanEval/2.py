
import math

def truncate_number(number: float) -> float:
    """ 
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than the given number) and 
    decimals (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Parameters:
    number (float): A positive floating point number.

    Returns:
    float: The decimal part of the number.

    Raises:
    ValueError: If the number is not a positive floating point number.

    Examples:
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(5.75)
    0.75
    >>> truncate_number(10.0)
    0.0
    """
    if not isinstance(number, float) or number < 0:
        raise ValueError("Input must be a positive floating point number.")
    
    integer_part = math.floor(number)  # Get the integer part
    decimal_part = number - integer_part  # Calculate the decimal part
    
    return decimal_part

# Example usage
if __name__ == "__main__":
    print(truncate_number(3.5))  # Output: 0.5
    print(truncate_number(5.75))  # Output: 0.75
    print(truncate_number(10.0))  # Output: 0.0
