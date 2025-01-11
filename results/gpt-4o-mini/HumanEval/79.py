
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format with 'db' characters."""
    # Convert decimal to binary and remove the '0b' prefix
    binary_representation = bin(decimal)[2:]
    # Format the string with 'db' at the beginning and end
    formatted_binary = f"db{binary_representation}db"
    return formatted_binary

# Example usage:
print(decimal_to_binary(15))   # returns "db1111db"
print(decimal_to_binary(32))   # returns "db100000db"
