
def triangle_area(a, h):
    """Calculate the area of a triangle given its base and height.

    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.

    Returns:
    float: The area of the triangle.

    Example:
    >>> triangle_area(5, 3)
    7.5
    """
    area = 0.5 * a * h
    return area


# Test the function with the provided example
base = 5
height = 3
area = triangle_area(base, height)
print(f"The area of the triangle with base {base} and height {height} is: {area}")
