
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    For a given list of integers, return a tuple consisting of the sum and product of all the integers in the list.
    An empty list should return a sum of 0 and a product of 1.
    
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:  # Check if the list is empty
        return (0, 1)  # Return sum as 0 and product as 1 for an empty list

    total_sum = sum(numbers)  # Calculate the sum of the list
    total_product = 1  # Initialize product to 1 (identity for multiplication)

    for number in numbers:
        total_product *= number  # Multiply each number to get the product

    return (total_sum, total_product)  # Return the sum and product as a tuple

# Example usage:
print(sum_product([]))             # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))   # Output: (10, 24)
print(sum_product([-1, 2, -3]))    # Output: (-2, 6)
