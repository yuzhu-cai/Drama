
def search(lst):
    from collections import Counter
    
    # Count the frequency of each integer in the list
    frequency = Counter(lst)
    
    # Initialize the result variable to -1 (default if no valid integer is found)
    result = -1
    
    # Iterate through the frequency dictionary
    for num, freq in frequency.items():
        # Check if the number is greater than zero and its frequency is greater than or equal to the number itself
        if num > 0 and freq >= num:
            # Update the result if the current number is greater than the current result
            result = max(result, num)
    
    return result


print(search([4, 1, 2, 2, 3, 1]))  # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Output: 3
print(search([5, 5, 4, 4, 4]))  # Output: -1
