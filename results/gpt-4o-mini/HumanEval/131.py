
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    has_odd = False
    
    for digit in str(n):
        digit = int(digit)
        if digit % 2 != 0:  # Check if the digit is odd
            product *= digit
            has_odd = True
            
    return product if has_odd else 0

# Example usage:
print(digits(1))   # Output: 1
print(digits(4))   # Output: 0
print(digits(235)) # Output: 15
