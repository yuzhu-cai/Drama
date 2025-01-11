
def smallest_change(arr):
    n = len(arr)
    changes = 0
    
    # Compare elements from the start and end moving towards the center
    for i in range(n // 2):
        if arr[i] != arr[n - 1 - i]:
            changes += 1
            
    return changes

# Example test cases
print(smallest_change([1, 2, 3, 5, 4, 7, 9, 6]))  # Output: 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2]))     # Output: 1
print(smallest_change([1, 2, 3, 2, 1]))            # Output: 0
