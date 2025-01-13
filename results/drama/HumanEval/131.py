
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Convert the number to a string to iterate through digits
    str_n = str(n)
    product = 1
    found_odd = False
    
    for digit in str_n:
        # Convert character back to integer
        num = int(digit)
        # Check if the digit is odd
        if num % 2 != 0:
            product *= num
            found_odd = True
    
    # If no odd digits were found, return 0
    if not found_odd:
        return 0
    
    return product

# Example usage:
print(digits(1))    # Output: 1 (odd digit: 1)
print(digits(4))    # Output: 0 (no odd digits)
print(digits(235))  # Output: 15 (odd digits: 3 and 5, 3 * 5 = 15)
print(digits(24680)) # Output: 0 (no odd digits)
print(digits(13579)) # Output: 945 (odd digits: 1, 3, 5, 7, 9; product = 945)
