
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def intersection(interval1, interval2):
    """Determine whether the length of the intersection of two intervals is a prime number."""
    # Unpack the intervals
    start1, end1 = interval1
    start2, end2 = interval2
    
    # Calculate the intersection
    start_intersection = max(start1, start2)
    end_intersection = min(end1, end2)
    
    # Check if there is an intersection
    if start_intersection > end_intersection:
        return "NO"  # No intersection
    
    # Calculate the length of the intersection
    length_of_intersection = end_intersection - start_intersection
    
    # Check if the length is a prime number
    return "YES" if is_prime(length_of_intersection) else "NO"

# Example usage:
print(intersection((1, 2), (2, 3)))  # Output: "NO"
print(intersection((-1, 1), (0, 4)))  # Output: "NO"
print(intersection((-3, -1), (-5, 5)))  # Output: "YES"
