
def move_one_ball(arr):
    """Determine if the array can be sorted by right shifts."""
    if not arr:  # If the array is empty, return True
        return True
    
    n = len(arr)
    break_count = 0
    
    for i in range(n):
        if arr[i] > arr[(i + 1) % n]:  # Check the current element with the next (circularly)
            break_count += 1
            
        if break_count > 1:  # More than one break means we can't sort it
            return False
            
    return True  # If we have 0 or 1 break, we can sort it

# Example usage
print(move_one_ball([3, 4, 5, 1, 2]))  # True
print(move_one_ball([3, 5, 4, 1, 2]))  # False
