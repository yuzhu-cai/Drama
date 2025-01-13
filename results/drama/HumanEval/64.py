
def vowels_count(s):
    """Count the number of vowels in a given string.
    
    Vowels are defined as 'a', 'e', 'i', 'o', 'u'. The letter 'y' is also
    considered a vowel only when it appears at the end of the string.
    
    Args:
        s (str): The input string to be analyzed.
    
    Returns:
        int: The count of vowels in the input string.
    
    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = 'aeiouAEIOU'
    count = 0
    length = len(s)
    
    for i, char in enumerate(s):
        if char in vowels:
            count += 1
        elif char.lower() == 'y' and i == length - 1:
            count += 1  # Count 'y' only if it's at the end of the string
            
    return count


# Test cases for the vowels_count function

# Test case 1: Basic input with lowercase vowels
assert vowels_count("hello") == 2  # 'e' and 'o' are vowels

# Test case 2: Input with uppercase vowels
assert vowels_count("HELLO") == 2  # 'E' and 'O' are vowels

# Test case 3: Mixed case input
assert vowels_count("HeLLo") == 2  # 'e' and 'o' are vowels

# Test case 4: No vowels
assert vowels_count("bcdfgh") == 0  # No vowels present

# Test case 5: Empty string
assert vowels_count("") == 0  # No vowels in an empty string

# Test case 6: String with all vowels
assert vowels_count("aeiouAEIOU") == 10  # All characters are vowels

# Test case 7: String with spaces and punctuation
assert vowels_count("Hello, World!") == 3  # 'e', 'o', 'o' are vowels

# Test case 8: Long string with mixed characters
assert vowels_count("This is a test string with vowels.") == 8  # 'i', 'i', 'a', 'e', 'i', 'o', 'e'

# Test case 9: 'y' at the end of the string
assert vowels_count("Fly") == 0  # 'y' is not counted as a vowel

# Test case 10: 'y' as a vowel at the end
assert vowels_count("Happy") == 2  # 'a' and 'y' are counted as vowels

# Test case 11: 'y' not at the end
assert vowels_count("Rhythm") == 0  # 'y' is not counted as a vowel

# Test case 12: String with numbers and special characters
assert vowels_count("12345!@#$%^&*()") == 0  # No vowels present

# Test case 13: Long string with repeated vowels
assert vowels_count("aaaaaaeeeeeeiiiiiiouuuuu") == 24  # All characters are vowels

# Test case 14: String with mixed content
assert vowels_count("The quick brown fox jumps over the lazy dog.") == 11  # 'e', 'u', 'i', 'o', 'o', 'u', 'o', 'e', 'e', 'a', 'o'

print("All test cases passed!")
