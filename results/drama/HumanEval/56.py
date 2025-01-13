
def correct_bracketing(brackets: str) -> bool:
    """ 
    Check if every opening bracket has a corresponding closing bracket.
    
    Args:
    brackets (str): A string consisting of '<' and '>'.
    
    Returns:
    bool: True if every opening bracket has a corresponding closing bracket, False otherwise.
    
    Examples:
    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    # Initialize a counter
    counter = 0
    
    # Iterate through each character in the string
    for char in brackets:
        if char == '<':
            counter += 1  # Increment for an opening bracket
        elif char == '>':
            counter -= 1  # Decrement for a closing bracket
            
        # If counter goes negative, there's an unmatched closing bracket
        if counter < 0:
            return False
    
    # At the end, the counter should be zero if all brackets are matched
    return counter == 0

# Example usage
if __name__ == "__main__":
    print(correct_bracketing("<"))        # False
    print(correct_bracketing("<>"))       # True
    print(correct_bracketing("<<><>>"))   # True
    print(correct_bracketing("><<>"))     # False
