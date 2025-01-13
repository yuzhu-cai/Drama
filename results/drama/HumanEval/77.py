
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    
    Parameters:
    a (int): The integer to check.
    
    Returns:
    bool: True if a is a perfect cube, False otherwise.
    
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    
    # Calculate the cube root and round it to the nearest integer
    if a < 0:
        n = round(-(-a) ** (1/3))  # For negative numbers
    else:
        n = round(a ** (1/3))  # For non-negative numbers
    
    # Check if the cube of n equals a
    return n ** 3 == a


print(iscube(1))    # True, because 1 = 1^3
print(iscube(2))    # False, because there is no integer n such that n^3 = 2
print(iscube(-1))   # True, because -1 = (-1)^3
print(iscube(64))   # True, because 64 = 4^3
print(iscube(0))    # True, because 0 = 0^3
print(iscube(180))  # False, because there is no integer n such that n^3 = 180
