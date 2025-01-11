
def max_fill(grid, capacity):
    import math
    
    total_lowerings = 0
    
    for row in grid:
        # Count the number of 1's in the current row
        water_units = sum(row)
        
        # Calculate how many times we need to lower the bucket for this well
        if water_units > 0:
            lowerings = math.ceil(water_units / capacity)
            total_lowerings += lowerings
    
    return total_lowerings

# Example usage:
print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))  # Output: 6
print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))  # Output: 5
print(max_fill([[0,0,0], [0,0,0]], 5))  # Output: 0
