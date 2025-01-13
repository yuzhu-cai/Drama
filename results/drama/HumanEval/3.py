
from typing import List

def below_zero(operations: List[int]) -> bool:
    """
    This function checks if the balance of a bank account falls below zero
    after a series of deposit and withdrawal operations.

    :param operations: List of integers representing deposit (positive) and withdrawal (negative) operations.
    :return: True if the balance falls below zero at any point, otherwise False.

    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    >>> below_zero([-1, 2, 3])
    True
    >>> below_zero([5, -10, 5])
    True
    >>> below_zero([0, 0, 0])
    False
    """
    balance = 0  # Starting balance

    for operation in operations:
        balance += operation  # Update balance with the current operation
        if balance < 0:  # Check if balance falls below zero
            return True  # Return True if it does

    return False  # Return False if balance never goes below zero

# Example usage
if __name__ == "__main__":
    print(below_zero([1, 2, 3]))  # Output: False
    print(below_zero([1, 2, -4, 5]))  # Output: True
    print(below_zero([-1, 2, 3]))  # Output: True
    print(below_zero([5, -10, 5]))  # Output: True
    print(below_zero([0, 0, 0]))  # Output: False
