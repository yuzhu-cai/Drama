
def simplify(x, n):
    """Simplifies the expression x * n and returns True if the product is a whole number, otherwise False.
    
    Args:
    x (str): A string representation of the first fraction in the form 'numerator/denominator'.
    n (str): A string representation of the second fraction in the form 'numerator/denominator'.
    
    Returns:
    bool: True if the product of the fractions is a whole number, False otherwise.
    """
    
    # Parse the fractions
    numerator_x, denominator_x = map(int, x.split('/'))
    numerator_n, denominator_n = map(int, n.split('/'))
    
    # Calculate the product of the fractions
    product_numerator = numerator_x * numerator_n
    product_denominator = denominator_x * denominator_n
    
    # Check if the product is a whole number
    return product_numerator % product_denominator == 0

# Example usage:
print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
print(simplify("7/10", "10/2")) # False
