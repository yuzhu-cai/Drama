
def max_fill(grid, capacity):
    import math
    
    # Step 1: Count the total number of water units (1s) in the grid
    total_water_units = 0
    for row in grid:
        total_water_units += sum(row)  # Count 1s in each row
    
    # Step 2: Calculate the number of times buckets need to be lowered
    if capacity <= 0:
        raise ValueError("Bucket capacity must be greater than zero.")
    
    # Calculate the number of buckets needed
    buckets_needed = math.ceil(total_water_units / capacity)
    
    # Step 3: Return the result
    return buckets_needed

# Example usage
grid1 = [[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]]
bucket_capacity1 = 1
print(max_fill(grid1, bucket_capacity1))  # Output: 6

grid2 = [[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]]
bucket_capacity2 = 2
print(max_fill(grid2, bucket_capacity2))  # Output: 5

grid3 = [[0, 0, 0], [0, 0, 0]]
bucket_capacity3 = 5
print(max_fill(grid3, bucket_capacity3))  # Output: 0
