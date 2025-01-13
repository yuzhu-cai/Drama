
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    Uppercase vowels are defined as 'A', 'E', 'I', 'O', 'U'.
    
    Parameters:
    s (str): The input string to be analyzed.
    
    Returns:
    int: The count of uppercase vowels found at even indices of the string.
    
    Examples:
    count_upper('aBCdEf') returns 1  # 'E' is at index 4
    count_upper('abcdefg') returns 0  # No uppercase vowels at even indices
    count_upper('dBBE') returns 0  # 'B' is at index 2, but not a vowel
    count_upper('A1B2C3D4E5F6G7H8I9J') returns 3  # 'A' at index 0, 'E' at index 8, 'I' at index 12
    """
    vowels = {'A', 'E', 'I', 'O', 'U'}  # Set of uppercase vowels
    count = 0  # Initialize count of uppercase vowels
    
    # Iterate through even indices of the string
    for i in range(0, len(s), 2):
        if s[i] in vowels:  # Check if the character at even index is an uppercase vowel
            count += 1  # Increment count if it is an uppercase vowel
            
    return count  # Return the final count

# Example usage
if __name__ == "__main__":
    print(count_upper('aBCdEf'))  # Output: 1
    print(count_upper('abcdefg'))  # Output: 0
    print(count_upper('dBBE'))     # Output: 0
    print(count_upper('A1B2C3D4E5F6G7H8I9J'))  # Output: 3
