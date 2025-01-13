
def encode_cyclic(s: str) -> str:
    """
    Returns an encoded string by cycling groups of three characters.
    """
    # Split string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Cycle elements in each group. If the group has fewer than 3 characters, it remains unchanged.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    
    # Join the groups back into a single string
    return "".join(groups)

def decode_cyclic(s: str) -> str:
    """
    Takes as input a string encoded with the encode_cyclic function.
    Returns the decoded string by reversing the encoding process.
    """
    # Split the encoded string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Reverse the cycling for each group
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    # Join the groups back into a single string
    return "".join(groups)

# Example usage
original_string = "abcdefghij"
encoded_string = encode_cyclic(original_string)
decoded_string = decode_cyclic(encoded_string)

print(f"Original: {original_string}")
print(f"Encoded: {encoded_string}")
print(f"Decoded: {decoded_string}")
