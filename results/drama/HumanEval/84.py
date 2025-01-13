
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    
    # Step 1: Calculate the sum of the digits
    digit_sum = sum(int(digit) for digit in str(N))
    
    # Step 2: Convert the sum to a binary string
    binary_string = bin(digit_sum)[2:]  # [2:] to remove the '0b' prefix
    
    return binary_string

# Example usage
print(solve(1000))  # Output: "1"
print(solve(150))   # Output: "110"
print(solve(147))   # Output: "1100"
