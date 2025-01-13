
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.

    Parameters:
    nums (List[int]): A list of integers.

    Returns:
    int: The minimum sum of any non-empty sub-array.

    Example:
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_sum = float('inf')  # Initialize to a very large number
    n = len(nums)

    # Iterate over all possible sub-arrays
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += nums[end]  # Sum the current sub-array
            if current_sum < min_sum:  # Update min_sum if current_sum is smaller
                min_sum = current_sum

    return min_sum


# Example cases
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))         # Output: -6
print(minSubArraySum([1, -1, 2, -2, 3]))    # Output: -2
