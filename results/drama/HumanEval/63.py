
def fibfib(n: int) -> int:
    """Compute the n-th element of the FibFib sequence efficiently using memoization."""
    
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    # Dictionary to store computed values
    memo = {0: 0, 1: 0, 2: 1}
    
    def fibfib_helper(n: int) -> int:
        # Check if the value is already computed
        if n in memo:
            return memo[n]
        
        # Compute the value recursively and store it in the memo dictionary
        memo[n] = fibfib_helper(n - 1) + fibfib_helper(n - 2) + fibfib_helper(n - 3)
        return memo[n]
    
    return fibfib_helper(n)

# Example usage
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24
