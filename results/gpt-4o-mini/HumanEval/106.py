
def factorial(num):
    """Helper function to calculate the factorial of a number."""
    if num == 0 or num == 1:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

def f(n):
    """Return a list of size n with specific values based on index."""
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:  # i is even
            result.append(factorial(i))
        else:  # i is odd
            result.append(i * (i + 1) // 2)  # sum of numbers from 1 to i
    return result

# Example usage:
print(f(5))  # Output: [1, 2, 6, 24, 15]
