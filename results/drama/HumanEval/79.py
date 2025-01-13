
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format and return it as a formatted string.

    Args:
        decimal (int): A non-negative integer to be converted to binary.

    Returns:
        str: A string representing the binary format of the decimal number,
              with 'db' added at the beginning and end.

    Raises:
        ValueError: If the input is not a non-negative integer.
    
    Examples:
        decimal_to_binary(15)   # returns "db1111db"
        decimal_to_binary(32)   # returns "db100000db"
    """
    # Input validation
    if not isinstance(decimal, int) or decimal < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Special case for 0
    if decimal == 0:
        return "db0db"
    
    # Convert decimal to binary
    binary_string = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_string = str(remainder) + binary_string
        decimal //= 2  # Use floor division to reduce the number
    
    # Format the binary string with 'db' at the beginning and end
    formatted_binary_string = 'db' + binary_string + 'db'
    
    return formatted_binary_string

# Example usage
print(decimal_to_binary(15))  # Output: "db1111db"
print(decimal_to_binary(32))  # Output: "db100000db"
print(decimal_to_binary(0))    # Output: "db0db"
