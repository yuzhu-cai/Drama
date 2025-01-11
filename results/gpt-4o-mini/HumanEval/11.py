
def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure both strings are of the same length
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length.")
    
    # Perform XOR operation
    result = []
    for bit_a, bit_b in zip(a, b):
        # XOR operation: '1' if bits are different, '0' if they are the same
        result.append('1' if bit_a != bit_b else '0')
    
    return ''.join(result)

# Example usage
print(string_xor('010', '110'))  # Output: '100'
