
def specialFilter(nums):
    def is_odd_digit(digit):
        return digit in {'1', '3', '5', '7', '9'}
    
    def first_and_last_digits_are_odd(num):
        str_num = str(abs(num))  # Convert to string and take absolute value
        first_digit = str_num[0]
        last_digit = str_num[-1]
        return is_odd_digit(first_digit) and is_odd_digit(last_digit)

    count = 0
    for num in nums:
        if num > 10 and first_and_last_digits_are_odd(num):
            count += 1
            
    return count

# Example usage:
print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 2
