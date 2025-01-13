
def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to be transformed.
        
    Returns:
        str: A new string with flipped case characters.
        
    Examples:
        >>> flip_case('Hello')
        'hELLO'
        >>> flip_case('Python Programming!')
        'pYTHON pROGRAMMING!'
        >>> flip_case('1234!@#$')
        '1234!@#$'  # Non-alphabetic characters remain unchanged
    """
    # Initialize an empty string to store the result
    flipped_string = ""
    
    # Iterate through each character in the input string
    for char in string:
        # Check if the character is lowercase
        if char.islower():
            # Convert to uppercase
            flipped_string += char.upper()
        # Check if the character is uppercase
        elif char.isupper():
            # Convert to lowercase
            flipped_string += char.lower()
        else:
            # If it's neither, just add the character as is
            flipped_string += char
            
    return flipped_string

# Example usage
if __name__ == "__main__":
    print(flip_case("Hello World!"))  # Output: hELLO wORLD!
