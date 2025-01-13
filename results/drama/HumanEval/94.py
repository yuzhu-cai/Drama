
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_digits(n):
    """Calculate the sum of the digits of a number."""
    return sum(int(digit) for digit in str(n))

def largest_prime_digit_sum(lst):
    """Find the largest prime number in the list and return the sum of its digits."""
    largest_prime = None
    
    for number in lst:
        if is_prime(number):
            if largest_prime is None or number > largest_prime:
                largest_prime = number
    
    if largest_prime is not None:
        return sum_of_digits(largest_prime)
    else:
        return 0  # Return 0 if there are no prime numbers

# Example usage:
test_cases = [
    [0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3],
    [1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1],
    [1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3],
    [0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6],
    [0, 81, 12, 3, 1, 21],
    [0, 8, 1, 2, 1, 7]
]

# Running the test cases
for case in test_cases:
    result = largest_prime_digit_sum(case)
    print(f"For the list {case}, the output is: {result}")
