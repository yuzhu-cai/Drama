
def rounded_avg(n, m):
    """Compute the average of integers from n to m, round it, and convert to binary.
    
    Args:
        n (int): The starting integer.
        m (int): The ending integer.
        
    Returns:
        str or int: The binary representation of the rounded average prefixed with '0b',
                     or -1 if n is greater than m.
    """
    # Check if n is greater than m
    if n > m:
        return -1
    
    # Calculate the average
    count = m - n + 1  # Number of integers from n to m
    total_sum = (count * (n + m)) // 2  # Sum of integers from n to m
    average = total_sum / count  # Calculate average
    
    # Round the average to the nearest integer
    rounded_average = round(average)
    
    # Convert the rounded average to binary format
    binary_representation = bin(rounded_average)  # Convert to binary with '0b' prefix
    
    return binary_representation

# Example usage
print(rounded_avg(1, 5))   # Output: "0b11"
print(rounded_avg(7, 5))   # Output: -1
print(rounded_avg(10, 20))  # Output: "0b1111"
print(rounded_avg(20, 33))  # Output: "0b11010"
