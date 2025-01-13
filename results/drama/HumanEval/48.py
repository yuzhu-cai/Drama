
def is_palindrome(text: str) -> bool:
    """
    Checks if the given string is a palindrome.
    
    A palindrome is a string that reads the same forwards and backwards,
    ignoring spaces and case differences.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Examples:
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    >>> is_palindrome('A man a plan a canal Panama')
    True
    >>> is_palindrome('No lemon, no melon')
    True
    >>> is_palindrome('Was it a car or a cat I saw?')
    True
    """
    # Normalize the string: remove spaces and convert to lower case
    normalized_str = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if the normalized string is the same as its reverse
    return normalized_str == normalized_str[::-1]

# Example usage:
if __name__ == "__main__":
    print(is_palindrome("A man a plan a canal Panama"))  # Output: True
    print(is_palindrome("No lemon, no melon"))            # Output: True
    print(is_palindrome("Was it a car or a cat I saw?")) # Output: True
    print(is_palindrome("Hello"))                          # Output: False
