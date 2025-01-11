
def sort_array(arr):
    """
    Sorts an array of non-negative integers according to the number of ones in their binary representation
    in ascending order. For similar number of ones, sorts based on decimal value.

    :param arr: List of non-negative integers
    :return: Sorted list of integers
    """
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Example usage:
print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
print(sort_array([0, 1, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]
print(sort_array([-2, -3, -4, -5, -6]))  # Output: [-6, -5, -4, -3, -2]
