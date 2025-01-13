
def is_palindrome(q):
    """Check if the list q is a palindrome."""
    return q == q[::-1]

def sum_of_elements(q):
    """Calculate the sum of the elements in the list q."""
    return sum(q)

def will_it_fly(q, w):
    """
    Determine if the object q will fly based on its balance and weight.
    
    An object will fly if:
    1. It is balanced (palindromic list).
    2. The sum of its elements is less than or equal to the maximum weight w.
    
    Args:
    q (list): The list of elements to check.
    w (int): The maximum possible weight.
    
    Returns:
    bool: True if the object will fly, False otherwise.
    """
    # Check if the list is a palindrome
    balanced = is_palindrome(q)
    
    # Calculate the sum of the elements
    total_sum = sum_of_elements(q)
    
    # Return True if both conditions are met
    return balanced and total_sum <= w

# Example usage:
print(will_it_fly([1, 2], 5))      # ➞ False
print(will_it_fly([3, 2, 3], 1))   # ➞ False
print(will_it_fly([3, 2, 3], 9))   # ➞ True
print(will_it_fly([3], 5))          # ➞ True
