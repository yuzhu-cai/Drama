
from collections import Counter

def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exists, return -1.
    
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    
    # Count the frequency of each integer in the list
    frequency = Counter(lst)
    
    # Initialize the variable to store the greatest integer
    greatest = -1  # Start with -1 to indicate no valid integer found
    
    # Iterate through the unique integers and their frequencies
    for num, freq in frequency.items():
        # Check if the frequency is greater than or equal to the integer's value
        if freq >= num:
            greatest = max(greatest, num)  # Update greatest if the condition is met
    
    return greatest  # Return the greatest integer found, or -1 if none exist

# Example usage
print(search([4, 1, 2, 2, 3, 1]))  # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Output: 3
print(search([5, 5, 4, 4, 4]))  # Output: -1
