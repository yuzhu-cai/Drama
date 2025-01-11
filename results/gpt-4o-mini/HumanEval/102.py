
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1  # Invalid range

    # Start from y and go down to x
    for num in range(y, x - 1, -1):
        if num % 2 == 0:  # Check if the number is even
            return num  # Return the first even number found

    return -1  # If no even number is found


print(choose_num(12, 15))  # Output: 14
print(choose_num(13, 12))  # Output: -1
print(choose_num(10, 20))  # Output: 20
print(choose_num(21, 25))  # Output: 24
