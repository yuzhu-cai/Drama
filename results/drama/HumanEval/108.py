
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """
    
    def sum_of_signed_digits(num):
        # Determine the sign of the first digit
        sign = -1 if num < 0 else 1
        # Calculate the sum of digits
        sum_digits = sum(int(digit) for digit in str(abs(num)))
        # Adjust the sum based on the sign
        return sign * sum_digits

    count = 0
    for num in arr:
        if sum_of_signed_digits(num) > 0:
            count += 1
            
    return count

# Example usage
print(count_nums([]))  # Output: 0
print(count_nums([-1, 11, -11]))  # Output: 1
print(count_nums([1, 1, 2]))  # Output: 3
