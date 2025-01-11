
def encrypt(s):
    """Encrypts a string by rotating each letter down the alphabet by 4 places."""
    encrypted_string = ""
    
    for char in s:
        if 'a' <= char <= 'z':  # Check if the character is a lowercase letter
            # Calculate the new character
            new_char = chr((ord(char) - ord('a') + 4) % 26 + ord('a'))
            encrypted_string += new_char
        else:
            # If the character is not a lowercase letter, we can choose to leave it unchanged
            encrypted_string += char
            
    return encrypted_string

# Test cases
print(encrypt('hi'))          # Should return 'lm'
print(encrypt('asdfghjkl'))   # Should return 'ewhjklnop'
print(encrypt('gf'))          # Should return 'kj'
print(encrypt('et'))          # Should return 'ix'
