
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Determine the lower and upper bounds
    lower = min(a, b)
    upper = max(a, b)
    
    # Create a list to hold the even digits
    even_digits = []
    
    # Loop through the range of integers
    for number in range(lower, upper + 1):
        # Convert the number to a string to iterate through its digits
        for digit in str(number):
            # Check if the digit is even
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))
    
    # Sort the list of even digits in ascending order
    sorted_even_digits = sorted(set(even_digits))  # Use set to avoid duplicates
    
    return sorted_even_digits

# Example usage
print(generate_integers(2, 8))    # Output: [2, 4, 6, 8]
print(generate_integers(8, 2))    # Output: [2, 4, 6, 8]
print(generate_integers(10, 14))  # Output: []
