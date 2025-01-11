
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:  # Check if the list is empty
        return (0, 1)  # Return (0, 1) for empty list

    total_sum = sum(numbers)  # Calculate the sum of the list
    total_product = 1  # Initialize product to 1

    for number in numbers:
        total_product *= number  # Calculate the product

    return (total_sum, total_product)  # Return the tuple of sum and product


print(sum_product([]))          # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
