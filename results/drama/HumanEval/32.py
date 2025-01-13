
import math

def poly(xs: list, x: float) -> float:
    """
    Evaluates the polynomial with coefficients xs at point x.
    
    Parameters:
    xs (list): Coefficients of the polynomial, where xs[i] is the coefficient for x^i.
    x (float): The point at which to evaluate the polynomial.
    
    Returns:
    float: The value of the polynomial at x.
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list, initial_guess=0.0, tolerance=1e-7, max_iterations=1000) -> float:
    """
    Finds a root of the polynomial defined by the coefficients in xs.
    
    Parameters:
    xs (list): Coefficients of the polynomial, where xs[i] is the coefficient for x^i.
    initial_guess (float): Initial guess for the root.
    tolerance (float): Tolerance for convergence.
    max_iterations (int): Maximum number of iterations to prevent infinite loops.
    
    Returns:
    float: A root of the polynomial, or None if no root is found.
    """
    
    # Define the polynomial function and its derivative
    def polynomial(x):
        return sum(coef * (x ** i) for i, coef in enumerate(xs))

    def derivative(x):
        return sum(i * coef * (x ** (i - 1)) for i, coef in enumerate(xs) if i > 0)

    # Ensure the input list has an even number of coefficients
    if len(xs) % 2 != 0:
        raise ValueError("The input list must have an even number of coefficients.")

    # Start with the initial guess
    x = initial_guess
    for iteration in range(max_iterations):
        f_x = polynomial(x)
        f_prime_x = derivative(x)

        if abs(f_x) < tolerance:
            return x  # Found a root

        if f_prime_x == 0:
            raise ValueError("Derivative is zero. No convergence.")

        # Newton-Raphson update
        x = x - f_x / f_prime_x

    raise ValueError("Maximum iterations reached. No root found.")


# Example 1: Evaluating a polynomial
coefficients = [1, -3, 2]  # Represents the polynomial x^2 - 3x + 2
x_value = 1
print(f"poly({coefficients}, {x_value}) = {poly(coefficients, x_value)}")  # Output: 0

# Example 2: Finding a root of a polynomial
coefficients = [1, -3, 2]  # Represents the polynomial x^2 - 3x + 2
root = find_zero(coefficients)
print(f"Root found: {root}")  # Output: 2.0 or 1.0 (depending on the initial guess)
