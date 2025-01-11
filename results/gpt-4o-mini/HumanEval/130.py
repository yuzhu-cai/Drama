
def tri(n):
    """Generate the first n + 1 numbers of the Tribonacci sequence."""
    # Initialize the list to hold the sequence values
    tribonacci_sequence = []
    
    # Calculate the values based on the given rules
    for i in range(n + 1):
        if i == 1:
            tribonacci_sequence.append(3)  # tri(1) = 3
        elif i == 0:
            tribonacci_sequence.append(1)  # tri(0) = 1
        elif i % 2 == 0:  # Even index
            tribonacci_sequence.append(1 + i / 2)
        else:  # Odd index
            # Calculate tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1)
            if i - 1 < len(tribonacci_sequence) and i - 2 < len(tribonacci_sequence):
                # We need to calculate tri(i + 1) as well
                if i + 1 < len(tribonacci_sequence):
                    tri_next = tribonacci_sequence[i + 1]
                else:
                    tri_next = 1 + (i + 1) / 2  # Calculate tri(i + 1) if not already in the list
                tri_value = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tri_next
                tribonacci_sequence.append(tri_value)
    
    return tribonacci_sequence

# Example usage
print(tri(3))  # Output: [1, 3, 2, 8]
