
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this integer is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    # Calculate the cube root of a
    cube_root = round(a ** (1/3))
    
    # Check if the cube of the rounded cube root equals a
    return cube_root ** 3 == a

# Test cases
print(iscube(1))    # True
print(iscube(2))    # False
print(iscube(-1))   # True
print(iscube(64))   # True
print(iscube(0))    # True
print(iscube(180))  # False
