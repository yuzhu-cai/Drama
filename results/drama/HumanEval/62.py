
def derivative(xs: list):
    """ 
    Calculate the derivative of a polynomial represented by a list of coefficients.
    
    The polynomial is represented as:
    P(x) = xs[0] + xs[1] * x + xs[2] * x^2 + ...
    
    The function returns the coefficients of the derivative polynomial.
    
    Parameters:
    xs (list): A list of coefficients [a_0, a_1, a_2, ..., a_n]
    
    Returns:
    list: A list of coefficients for the derivative of the polynomial.
    
    Examples:
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative coefficients list
    derivative_coeffs = []
    
    # Iterate over the coefficients, excluding the last one (constant term)
    for i in range(len(xs) - 1):
        # The derivative of a_i * x^i is i * a_i * x^(i-1)
        derivative_coeffs.append(xs[i] * (len(xs) - 1 - i))
    
    return derivative_coeffs

# Testing the function with provided examples
if __name__ == "__main__":
    # Test cases
    print(derivative([3, 1, 2, 4, 5]))  # Expected output: [1, 4, 12, 20]
    print(derivative([1, 2, 3]))        # Expected output: [2, 6]
