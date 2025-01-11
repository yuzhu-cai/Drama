
def is_simple_power(x, n):
    # Handle edge cases
    if n <= 1:
        return x == n  # n=1 only works for x=1, n=0 is not valid for powers
    if x < 1:
        return False  # x must be at least 1 for any positive power

    # Start with k = 0 and calculate n^k until it exceeds x
    k = 0
    while True:
        power = n ** k
        if power == x:
            return True
        if power > x:
            return False
        k += 1

# Example usage:
print(is_simple_power(1, 4))  # True
print(is_simple_power(2, 2))  # True
print(is_simple_power(8, 2))  # True
print(is_simple_power(3, 2))  # False
print(is_simple_power(3, 1))  # False
print(is_simple_power(5, 3))  # False
