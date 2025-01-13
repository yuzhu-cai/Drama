
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle, return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is a right angle (90 degrees).
    
    Parameters:
    a (float): Length of side a
    b (float): Length of side b
    c (float): Length of side c

    Returns:
    bool: True if the sides form a right-angled triangle, False otherwise.
    
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    
    # Sort the sides to identify the longest side
    sides = sorted([a, b, c])
    
    # Check the Pythagorean theorem condition
    return sides[0]**2 + sides[1]**2 == sides[2]**2

# Example usage
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False
