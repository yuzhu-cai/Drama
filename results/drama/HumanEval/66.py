
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the uppercase characters' ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    cumulative_sum = 0  # Initialize the cumulative sum to zero
    for char in s:  # Iterate through each character in the string
        if char.isupper():  # Check if the character is uppercase
            cumulative_sum += ord(char)  # Add the ASCII value of the uppercase character to the sum
    return cumulative_sum  # Return the final cumulative sum

# Example usage
print(digitSum(""))  # Output: 0
print(digitSum("abAB"))  # Output: 131
print(digitSum("abcCd"))  # Output: 67
print(digitSum("helloE"))  # Output: 69
print(digitSum("woArBld"))  # Output: 131
print(digitSum("aAaaaXa"))  # Output: 153
