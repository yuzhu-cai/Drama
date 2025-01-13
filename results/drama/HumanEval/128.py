
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr:  # Check if the array is empty
        return None

    sum_of_magnitudes = sum(abs(num) for num in arr)  # Calculate the sum of magnitudes
    product_of_signs = 1  # Initialize product of signs

    for num in arr:
        if num < 0:
            product_of_signs *= -1  # Flip the sign for negative numbers
        elif num == 0:
            return 0  # If any number is zero, return 0 immediately

    return sum_of_magnitudes * product_of_signs  # Return the final result

# Example usage:
print(prod_signs([1, 2, 2, -4]))  # Output: -9
print(prod_signs([0, 1]))          # Output: 0
print(prod_signs([]))              # Output: None
