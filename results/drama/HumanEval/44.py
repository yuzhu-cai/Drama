
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base.
    Return string representation after the conversion.
    Base numbers must be less than 10.
    
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    
    # Validate the base
    if base < 2 or base >= 10:
        raise ValueError("Base must be between 2 and 9 (inclusive).")
    
    if x == 0:
        return "0"
    
    negative = x < 0
    x = abs(x)
    digits = []
    
    while x > 0:
        remainder = x % base
        digits.append(str(remainder))
        x //= base
    
    # Reverse the digits to get the correct order
    digits.reverse()
    
    # Join the digits to form the final string representation
    result = ''.join(digits)
    
    return '-' + result if negative else result

# Example usage and testing
if __name__ == "__main__":
    print(change_base(8, 3))  # Output: '22'
    print(change_base(8, 2))  # Output: '1000'
    print(change_base(7, 2))  # Output: '111'
    print(change_base(0, 3))  # Output: '0'
    print(change_base(-8, 3)) # Output: '-22'
