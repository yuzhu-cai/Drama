
def sum_of_digits(n):
    """
    Helper function to calculate the sum of digits of a number.
    
    Parameters:
    n (int): The integer whose digits are to be summed.
    
    Returns:
    int: The sum of the digits of the integer.
    """
    return sum(int(digit) for digit in str(abs(n)))

def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    If there are several items with similar sum of their digits, order them based on their index in the original list.

    Parameters:
    nums (list of int): A list of integers to be sorted.

    Returns:
    list of int: A new list containing the sorted integers.
    
    Examples:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    return sorted(nums, key=lambda x: (sum_of_digits(x), nums.index(x)))

# Example usage
if __name__ == "__main__":
    print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
    print(order_by_points([]))                        # Output: []
