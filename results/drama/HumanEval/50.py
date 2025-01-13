
def encode_shift(s: str) -> str:
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([
        chr(((ord(ch) - ord('a') + 5) % 26) + ord('a')) if ch.islower() else
        chr(((ord(ch) - ord('A') + 5) % 26) + ord('A')) if ch.isupper() else ch
        for ch in s
    ])


def decode_shift(s: str) -> str:
    """
    Takes as input a string encoded with encode_shift function. Returns decoded string.
    """
    decoded_str = ""
    for char in s:
        if char.isalpha():  # Check if the character is a letter
            # Determine the ASCII offset based on uppercase or lowercase
            offset = ord('A') if char.isupper() else ord('a')
            # Decode the character and wrap around using modulo
            decoded_char = chr((ord(char) - offset - 5) % 26 + offset)
            decoded_str += decoded_char
        else:
            # Non-alphabetic characters are added unchanged
            decoded_str += char
    return decoded_str


# Example usage
original_message = "Hello, World!"
encoded_message = encode_shift(original_message)
print(f"Encoded: {encoded_message}")  # Encoded message

decoded_message = decode_shift(encoded_message)
print(f"Decoded: {decoded_message}")  # Should match original message
