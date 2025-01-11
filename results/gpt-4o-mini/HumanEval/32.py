
import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])

def find_zero(xs: list):
    """ 
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having an even number of coefficients
    and the largest non-zero coefficient as it guarantees a solution.
    
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Check if the number of coefficients is even
    if len(xs) % 2 != 0:
        raise ValueError("The number of coefficients must be even.")
    
    # Define the interval for the bisection method
    lower_bound = -1000  # A reasonable lower bound
    upper_bound = 1000   # A reasonable upper bound

    # Check if the function changes sign in the interval
    f_lower = poly(xs, lower_bound)
    f_upper = poly(xs, upper_bound)

    if f_lower * f_upper > 0:
        raise ValueError("The function must change signs over the interval.")

    # Bisection method
    while upper_bound - lower_bound > 1e-7:  # Precision threshold
        midpoint = (lower_bound + upper_bound) / 2
        f_mid = poly(xs, midpoint)

        if f_mid == 0:
            return midpoint  # Found exact root
        elif f_mid * f_lower < 0:
            upper_bound = midpoint
            f_upper = f_mid
        else:
            lower_bound = midpoint
            f_lower = f_mid

    return (lower_bound + upper_bound) / 2  # Return the midpoint as the root

# Example usage
if __name__ == "__main__":
    print(round(find_zero([1, 2]), 2))  # Output: -0.5
    print(round(find_zero([-6, 11, -6, 1]), 2))  # Output: 1.0
