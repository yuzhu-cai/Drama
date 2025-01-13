
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    # Ensure x is less than or equal to y
    if x > y:
        return -1
    
    # Start from the largest number in the range and check for evenness
    for num in range(y, x - 1, -1):
        if num % 2 == 0:
            return num  # Return the first even number found
    
    # If no even integer is found, return -1
    return -1

# Example usage:
print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1
print(choose_num(5, 10))   # Output: 10
print(choose_num(3, 3))    # Output: -1
