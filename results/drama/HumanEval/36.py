
def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    total_count = 0
    
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            total_count += str(i).count('7')
    
    return total_count

# Example usage
if __name__ == "__main__":
    print(fizz_buzz(50))  # Output: 0
    print(fizz_buzz(78))  # Output: 2
    print(fizz_buzz(79))  # Output: 3
