
def maximum(arr, k):
    # Step 1: Sort the array in descending order
    sorted_arr = sorted(arr, reverse=True)
    
    # Step 2: Select the first k elements
    max_k_elements = sorted_arr[:k]
    
    # Step 3: Sort the selected k elements in ascending order
    return sorted(max_k_elements)

# Example usage:
print(maximum([-3, -4, 5], 3))  # Output: [-4, -3, 5]
print(maximum([4, -4, 4], 2))    # Output: [4, 4]
print(maximum([-3, 2, 1, 2, -1, -2, 1], 1))  # Output: [2]
