
from typing import List

def max_nesting_level(s: str) -> int:
    """Helper function to calculate the maximum nesting level of parentheses in a single string."""
    max_level = 0
    current_level = 0

    for char in s:
        if char == '(':
            current_level += 1
            max_level = max(max_level, current_level)
        elif char == ')':
            current_level -= 1
            if current_level < 0:
                raise ValueError("Unmatched closing parenthesis found.")

    if current_level > 0:
        raise ValueError("Unmatched opening parenthesis found.")

    return max_level

def parse_nested_parens(paren_string: str) -> List[int]:
    """Parse a string of nested parentheses groups and return their maximum nesting levels.

    Args:
        paren_string (str): A string containing groups of nested parentheses separated by spaces.

    Returns:
        List[int]: A list of maximum nesting levels for each group.

    Examples:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    # Split the input string by spaces to get individual groups
    groups = paren_string.split()
    
    # Calculate the maximum nesting level for each group
    max_levels = []
    for group in groups:
        max_levels.append(max_nesting_level(group))

    return max_levels

# Example usage
if __name__ == "__main__":
    result = parse_nested_parens('(()()) ((())) () ((())()())')
    print(result)  # Output: [2, 3, 1, 3]
