
def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_up_to(n):
    """Return an array of the first n integers that are prime numbers and less than n."""
    primes = []
    for num in range(2, n):  # Start from 2 and go up to n-1
        if is_prime(num):
            primes.append(num)
    return primes

# Example usage
print(count_up_to(5))   # Output: [2, 3]
print(count_up_to(11))  # Output: [2, 3, 5, 7]
print(count_up_to(0))   # Output: []
print(count_up_to(20))  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
print(count_up_to(1))   # Output: []
print(count_up_to(18))  # Output: [2, 3, 5, 7, 11, 13, 17]
