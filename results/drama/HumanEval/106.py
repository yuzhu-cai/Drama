
import math

def f(n):
    """ 
    Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    """
    result_list = []  # Initialize an empty list to store results

    for i in range(1, n + 1):  # Iterate from 1 to n (inclusive)
        if i % 2 == 0:  # Check if i is even
            factorial = math.factorial(i)  # Calculate factorial of i
            result_list.append(factorial)  # Store in the list
        else:  # i is odd
            total_sum = (i * (i + 1)) // 2  # Calculate sum from 1 to i
            result_list.append(total_sum)  # Store in the list

    return result_list  # Return the completed list

# Example usage
print(f(5))  # Output: [1, 2, 6, 24, 15]
