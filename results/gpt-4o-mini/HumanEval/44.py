
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x == 0:
        return '0'
    
    digits = []
    
    while x > 0:
        remainder = x % base
        digits.append(str(remainder))
        x //= base
    
    # The digits are collected in reverse order, so we need to reverse them
    digits.reverse()
    
    return ''.join(digits)

# Example usage:
print(change_base(8, 3))  # Output: '22'
print(change_base(8, 2))  # Output: '1000'
print(change_base(7, 2))  # Output: '111'
