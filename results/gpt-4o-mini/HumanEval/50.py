
def decode_shift(s: str):
    """
    Takes as input a string encoded with the encode_shift function. Returns the decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])

def decode_shift(s: str):
    """
    Takes as input a string encoded with the encode_shift function. Returns the decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

# Example usage:
encoded = encode_shift("hello")
print("Encoded:", encoded)  # Encoded: mjqqt
decoded = decode_shift(encoded)
print("Decoded:", decoded)  # Decoded: hello
