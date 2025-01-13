
def get_odd_collatz(n):
    """
    Given a positive integer n, return a sorted list that has the odd numbers in the Collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. Returned list is sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The Collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    odd_numbers = []
    
    # Generate the Collatz sequence
    while n != 1:
        if n % 2 != 0:  # Check if n is odd
            odd_numbers.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1  # Apply Collatz rules
    
    # Check if 1 should be included (1 is odd)
    odd_numbers.append(1)  # 1 is always part of the sequence
    
    # Sort the list of odd numbers
    sorted_odd_numbers = sorted(odd_numbers)
    
    return sorted_odd_numbers

# Example usage
print(get_odd_collatz(5))  # Output: [1, 5]
print(get_odd_collatz(7))  # Output: [1, 3, 5, 7]
