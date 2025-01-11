
def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Convert the number to its absolute value and then to a string
    num_str = str(abs(num))
    
    even_count = 0
    odd_count = 0
    
    # Iterate through each character in the string representation of the number
    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    return (even_count, odd_count)

# Example usage:
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))   # Output: (1, 2)
