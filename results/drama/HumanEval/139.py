
def factorial(num):
    """Calculate the factorial of a non-negative integer num."""
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def special_factorial(n):
    """Calculate the Brazilian factorial of n."""
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    product = 1
    for i in range(1, n + 1):
        product *= factorial(i)
    
    return product

# Example usage
if __name__ == "__main__":
    n = 4
    result = special_factorial(n)
    print(f"The Brazilian factorial of {n} is: {result}")
