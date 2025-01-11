
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    
    Example:
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # Initialize the minimum sum to a large value
    min_sum = float('inf')
    current_sum = 0
    
    for num in nums:
        current_sum += num
        # Update the minimum sum if the current sum is less than the minimum found so far
        min_sum = min(min_sum, current_sum)
        # If the current sum is positive, reset it to 0
        if current_sum > 0:
            current_sum = 0
            
    return min_sum

# Example usage:
print(minSubArraySum([2, 3, 4, 1, 2, 4]))  # Output: 1
print(minSubArraySum([-1, -2, -3]))          # Output: -6
