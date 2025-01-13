
def are_first_and_last_digits_odd(number):
    """Check if the first and last digits of the number are both odd."""
    num_str = str(abs(number))  # Use absolute value to handle negative numbers
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    return first_digit % 2 != 0 and last_digit % 2 != 0

def specialFilter(nums):
    """Count the numbers that are greater than 10 and have both first and last digits odd."""
    count = 0
    for num in nums:
        if num > 10 and are_first_and_last_digits_odd(num):
            count += 1
    return count

# Example usage
print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2
