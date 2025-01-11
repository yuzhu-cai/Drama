
def even_odd_palindrome(n):
    def is_palindrome(num):
        # Convert the number to string and check if it reads the same forwards and backwards
        return str(num) == str(num)[::-1]

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
print(even_odd_palindrome(3))  # Output: (1, 2)
print(even_odd_palindrome(12)) # Output: (4, 6)
