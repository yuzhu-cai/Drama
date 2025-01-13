
def get_max_triples(n):
    # Step 1: Create the integer array a
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Step 2: Count occurrences of each remainder when divided by 3
    count0 = count1 = count2 = 0
    
    for num in a:
        if num % 3 == 0:
            count0 += 1
        elif num % 3 == 1:
            count1 += 1
        else:
            count2 += 1
            
    # Step 3: Calculate the number of valid triples
    def comb(n, r):
        if n < r:
            return 0
        if r == 3:
            return (n * (n - 1) * (n - 2)) // 6
        return 0
    
    # Count triples from the same category
    total_triples = comb(count0, 3) + comb(count1, 3) + comb(count2, 3)
    
    # Count triples from different categories
    total_triples += count0 * count1 * count2
    
    return total_triples

# Example usage
n = 5
result = get_max_triples(n)
print(result)  # Output: 1
