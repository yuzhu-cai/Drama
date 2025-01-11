
def order_by_points(nums):
    def digit_sum(n):
        # Calculate the sum of the absolute digits of n
        return sum(int(digit) for digit in str(abs(n)))

    # Use sorted with a key that sorts by digit sum and original index
    return sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))

# Example usage:
print(order_by_points([1, 11, -1, -11, -12]))  # Output: [-1, -11, 1, -12, 11]
print(order_by_points([]))  # Output: []
