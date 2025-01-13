
def reverse_delete(s, c):
    """Remove characters from s that are in c and check if the result is a palindrome.
    
    Args:
    s (str): The original string from which characters will be removed.
    c (str): The string containing characters to be removed from s.
    
    Returns:
    tuple: A tuple containing the resulting string and a boolean indicating if it's a palindrome.
    """
    # Create a set of characters to remove for efficient lookup
    chars_to_remove = set(c)
    
    # Create the resulting string by filtering out unwanted characters
    result_string = ''.join([char for char in s if char not in chars_to_remove])
    
    # Check if the resulting string is a palindrome
    is_palindrome = result_string == result_string[::-1]
    
    # Return the resulting string and the palindrome check result as a tuple
    return (result_string, is_palindrome)

# Example usage
print(reverse_delete("abcde", "ae"))        # Output: ('bcd', False)
print(reverse_delete("abcdef", "b"))         # Output: ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))     # Output: ('cdedc', True)
