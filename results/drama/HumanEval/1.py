
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ 
    Input to this function is a string containing multiple groups of nested parentheses. 
    The goal is to separate those groups into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Spaces in the input string are ignored.
    
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []  # List to store the separated groups
    current_group = []  # Temporary list to build the current group
    balance = 0  # To track the balance of parentheses

    # Iterate through each character in the input string
    for char in paren_string:
        if char == '(':  # If we encounter an opening parenthesis
            balance += 1
            current_group.append(char)  # Add it to the current group
        elif char == ')':  # If we encounter a closing parenthesis
            balance -= 1
            current_group.append(char)  # Add it to the current group

        # When balance is zero, we have a complete group
        if balance == 0 and current_group:
            groups.append(''.join(current_group))  # Join current group and add to groups
            current_group = []  # Reset current group for the next group

    return groups

# Example usage
if __name__ == "__main__":
    print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
