
def is_palindrome(num):
    """Check if a number is a palindrome."""
    str_num = str(num)
    return str_num == str_num[::-1]

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    
    :param n: Positive integer (1 <= n <= 1000)
    :return: Tuple (count_of_even_palindromes, count_of_odd_palindromes)
    """
    even_count = 0
    odd_count = 0
    
    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
    return (even_count, odd_count)

# Example usage:
print(even_odd_palindrome(3))   # Output: (1, 2)
print(even_odd_palindrome(12))  # Output: (4, 6)
