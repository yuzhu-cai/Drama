
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    # Extract the first k elements
    first_k_elements = arr[:k]
    
    # Initialize the sum
    total_sum = 0
    
    # Iterate through the first k elements and sum those with at most two digits
    for num in first_k_elements:
        if -99 <= num <= 99:  # Check if the number has at most two digits
            total_sum += num
            
    return total_sum

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print("The sum of elements with at most two digits from the first k elements is:", result)
