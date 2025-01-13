
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    # Extracting the unit digits
    unit_digit_a = abs(a) % 10  # Use abs to handle negative numbers
    unit_digit_b = abs(b) % 10  # Use abs to handle negative numbers
    
    # Calculating the product of the unit digits
    product = unit_digit_a * unit_digit_b
    
    return product

# Test cases
print(multiply(148, 412))  # Output: 16
print(multiply(19, 28))    # Output: 72
print(multiply(2020, 1851))  # Output: 0
print(multiply(14, -15))   # Output: 20
