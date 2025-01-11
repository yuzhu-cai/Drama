
import math

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(2.75)
    0.75
    >>> truncate_number(5.0)
    0.0
    >>> truncate_number(0.123)
    0.123
    """
    if number < 0:
        raise ValueError("The number must be positive.")
    
    integer_part = math.floor(number)
    decimal_part = number - integer_part
    return decimal_part
