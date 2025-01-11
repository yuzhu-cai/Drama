
def rounded_avg(n, m):
    """Compute the average of integers from n to m, round it, and convert to binary."""
    if n > m:
        return -1
    
    # Calculate the sum of integers from n to m
    total_sum = sum(range(n, m + 1))
    count = m - n + 1  # Total numbers from n to m
    
    # Calculate the average and round it
    average = total_sum / count
    rounded_average = round(average)
    
    # Convert to binary
    binary_representation = bin(rounded_average)
    
    return binary_representation

# Example usage:
print(rounded_avg(1, 5))  # Output: "0b11"
print(rounded_avg(7, 5))  # Output: -1
print(rounded_avg(10, 20))  # Output: "0b1111"
print(rounded_avg(20, 33))  # Output: "0b11010"
