
def sum_squares(lst):
    """
    This function takes a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1, 2, 3] the output should be 6
    For lst = [] the output should be 0
    For lst = [-1, -5, 2, -1, -5] the output should be -126
    """
    total = 0  # Initialize the total sum
    for index, value in enumerate(lst):
        if index % 3 == 0:  # Check if index is a multiple of 3
            total += value ** 2  # Square the integer and add to total
        elif index % 4 == 0:  # Check if index is a multiple of 4
            total += value ** 3  # Cube the integer and add to total
        else:
            total += value  # Add the integer as is if no modification is needed
    return total  # Return the final sum

# Example usage
print(sum_squares([1, 2, 3]))  # Output: 6
print(sum_squares([]))          # Output: 0
print(sum_squares([-1, -5, 2, -1, -5]))  # Output: -126
