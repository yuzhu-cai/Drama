
def count_nums(arr):
    def sum_of_digits(n):
        # Convert the number to a string and handle the sign
        str_n = str(n)
        # Initialize the sum
        digit_sum = 0
        
        # Iterate through each character in the string representation
        for i, char in enumerate(str_n):
            if char.isdigit():
                digit_sum += int(char)
            elif i == 0 and char == '-':
                digit_sum -= 1  # First signed digit is negative
        
        return digit_sum

    # Count how many numbers have a sum of digits > 0
    count = 0
    for number in arr:
        if sum_of_digits(number) > 0:
            count += 1
            
    return count

# Test cases
print(count_nums([]))  # Output: 0
print(count_nums([-1, 11, -11]))  # Output: 1
print(count_nums([1, 1, 2]))  # Output: 3
