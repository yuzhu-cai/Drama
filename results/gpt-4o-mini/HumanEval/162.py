
import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    if text == "":
        return None
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    # Update the hash object with the bytes of the string
    md5_hash.update(text.encode('utf-8'))
    # Return the hexadecimal digest of the hash
    return md5_hash.hexdigest()

# Example usage
if __name__ == "__main__":
    print(string_to_md5('Hello world'))  # Output: 3e25960a79dbc69b674cd4ec67a72c62
