
def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two input strings a and b consisting only of 1s and 0s.
    
    If the strings are of different lengths, the shorter string is padded with leading zeros.
    
    Parameters:
    a (str): A binary string consisting of '1's and '0's.
    b (str): A binary string consisting of '1's and '0's.
    
    Returns:
    str: A binary string representing the result of the XOR operation.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    >>> string_xor('101', '001')
    '100'
    >>> string_xor('1', '0001')
    '0000'
    """
    # Pad the shorter string with leading zeros
    max_length = max(len(a), len(b))
    a = a.zfill(max_length)
    b = b.zfill(max_length)

    # Perform XOR operation
    result = []
    for bit_a, bit_b in zip(a, b):
        result.append('1' if bit_a != bit_b else '0')

    return ''.join(result)

# Example usage
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output: '100'
    print(string_xor('101', '001'))  # Output: '100'
    print(string_xor('1', '0001'))    # Output: '0000'
