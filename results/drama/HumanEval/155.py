
def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert the number to a string to iterate through each digit
    str_num = str(num)
    
    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0
    
    # Loop through each character in the string representation of the number
    for char in str_num:
        # Check if the character is a digit (to handle negative signs)
        if char.isdigit():
            digit = int(char)
            if digit % 2 == 0:
                even_count += 1  # Increment even counter
            else:
                odd_count += 1   # Increment odd counter
    
    # Return the counts as a tuple
    return (even_count, odd_count)

# Example usage
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))   # Output: (1, 2)
print(even_odd_count(456789)) # Output: (3, 3)
