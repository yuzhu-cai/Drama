
def decode_cyclic(s: str):
    """
    Takes as input a string encoded with the encode_cyclic function. Returns the decoded string.
    """
    # Split the string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Reverse the cycling for each group
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    return "".join(groups)


encoded = encode_cyclic("abcdefg")  # "bcadefg"
decoded = decode_cyclic(encoded)     # "abcdefg"

print(encoded)  # Output: "bcadefg"
print(decoded)  # Output: "abcdefg"
