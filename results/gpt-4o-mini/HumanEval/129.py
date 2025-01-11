
from collections import deque

def minPath(grid, k):
    N = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    min_path = None
    
    for start_row in range(N):
        for start_col in range(N):
            # BFS initialization
            queue = deque([(start_row, start_col, [grid[start_row][start_col]])])
            
            while queue:
                row, col, path = queue.popleft()
                
                # If we reached the desired path length
                if len(path) == k:
                    if min_path is None or path < min_path:
                        min_path = path
                    continue
                
                # Explore neighbors
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < N and 0 <= new_col < N:
                        new_path = path + [grid[new_row][new_col]]
                        queue.append((new_row, new_col, new_path))
    
    return min_path

# Example usage:
grid1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
k1 = 3
print(minPath(grid1, k1))  # Output: [1, 2, 1]

grid2 = [[5, 9, 3], [4, 1, 6], [7, 8, 2]]
k2 = 1
print(minPath(grid2, k2))  # Output: [1]
