
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions."""
    total_sum = 0
    for index in range(len(lst)):
        if index % 2 == 0:  # Check if the index is even
            if lst[index] % 2 != 0:  # Check if the element is odd
                total_sum += lst[index]  # Add to total sum
    return total_sum

# Example test cases
print(solution([5, 8, 7, 1]))  # Output: 12
print(solution([3, 3, 3, 3, 3]))  # Output: 9
print(solution([30, 13, 24, 321]))  # Output: 0
