
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    
    # Check if the input list is empty
    if not lst:
        return 0
    
    # Filter the list to keep only non-negative integers
    filtered_list = [num for num in lst if isinstance(num, int) and num >= 0]
    
    # Identify odd numbers and calculate their squares
    odd_squares = [num ** 2 for num in filtered_list if num % 2 != 0]
    
    # Return the sum of the squares of odd numbers
    return sum(odd_squares)

# Example usage:
print(double_the_difference([1, 3, 2, 0]))  # Output: 10
print(double_the_difference([-1, -2, 0]))    # Output: 0
print(double_the_difference([9, -2]))         # Output: 81
print(double_the_difference([0]))              # Output: 0
print(double_the_difference([]))               # Output: 0
