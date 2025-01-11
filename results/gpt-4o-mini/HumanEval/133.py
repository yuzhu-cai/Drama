
import math

def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    # Round each number up to the nearest integer and square it
    squared_sum = sum(math.ceil(x) ** 2 for x in lst)
    return squared_sum

# Example usage:
print(sum_squares([1, 2, 3]))        # Output: 14
print(sum_squares([1, 4, 9]))        # Output: 98
print(sum_squares([1, 3, 5, 7]))     # Output: 84
print(sum_squares([1.4, 4.2, 0]))    # Output: 29
print(sum_squares([-2.4, 1, 1]))     # Output: 6
