
def reverse_delete(s, c):
    # Create a set of characters to delete for faster lookup
    chars_to_delete = set(c)
    
    # Create the result string by filtering out characters in chars_to_delete
    result = ''.join(char for char in s if char not in chars_to_delete)
    
    # Check if the result string is a palindrome
    is_palindrome = result == result[::-1]
    
    # Return the result string and the palindrome check
    return (result, is_palindrome)

# Example usage:
print(reverse_delete("abcde", "ae"))  # Output: ('bcd', False)
print(reverse_delete("abcdef", "b"))   # Output: ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # Output: ('cdedc', True)
