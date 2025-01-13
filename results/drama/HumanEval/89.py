
def rotate_character(char, rotation):
    """Rotate a single character by a specified rotation amount."""
    if char.isalpha():  # Check if the character is a letter
        # Determine the ASCII offset based on whether the character is uppercase or lowercase
        offset = ord('A') if char.isupper() else ord('a')
        # Rotate the character and wrap around using modulo
        return chr((ord(char) - offset + rotation) % 26 + offset)
    else:
        return char  # Non-alphabetic characters remain unchanged

def encrypt(s):
    """Encrypt the input string by rotating each letter down by 4 places."""
    rotation_amount = 4  # Each letter is shifted down by 4 places
    encrypted_string = ''.join(rotate_character(char, rotation_amount) for char in s)
    return encrypted_string

# Example usage
print(encrypt('hi'))          # Output: 'lm'
print(encrypt('asdfghjkl'))   # Output: 'ewhjklnop'
print(encrypt('gf'))          # Output: 'kj'
print(encrypt('et'))          # Output: 'ix'
