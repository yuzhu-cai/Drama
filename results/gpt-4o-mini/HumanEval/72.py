
def will_it_fly(q, w):
    '''
    Returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) 
    and the sum of its elements is less than or equal to the maximum possible weight w.
    '''
    # Check if the list is a palindrome
    is_balanced = q == q[::-1]
    
    # Calculate the sum of the elements in the list
    total_weight = sum(q)
    
    # Check if the total weight is less than or equal to w
    weight_check = total_weight <= w
    
    # The object will fly if both conditions are met
    return is_balanced and weight_check

# Example test cases
print(will_it_fly([1, 2], 5))  # ➞ False
print(will_it_fly([3, 2, 3], 1))  # ➞ False
print(will_it_fly([3, 2, 3], 9))  # ➞ True
print(will_it_fly([3], 5))  # ➞ True
