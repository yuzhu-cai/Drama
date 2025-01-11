
def get_max_triples(n):
    # Step 1: Generate the array a
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Step 2: Calculate remainders
    remainder_count = [0, 0, 0]  # Counts for remainders 0, 1, and 2
    for value in a:
        remainder_count[value % 3] += 1
    
    # Step 3: Count valid triples
    count = 0
    
    # Case 1: All three numbers have remainder 0
    count += (remainder_count[0] * (remainder_count[0] - 1) * (remainder_count[0] - 2)) // 6
    
    # Case 2: All three numbers have remainder 1
    count += (remainder_count[1] * (remainder_count[1] - 1) * (remainder_count[1] - 2)) // 6
    
    # Case 3: All three numbers have remainder 2
    count += (remainder_count[2] * (remainder_count[2] - 1) * (remainder_count[2] - 2)) // 6
    
    # Case 4: One from each remainder category
    count += remainder_count[0] * remainder_count[1] * remainder_count[2]
    
    return count

# Example usage:
print(get_max_triples(5))  # Output: 1
