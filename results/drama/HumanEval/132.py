
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    
    counter = 0  # Initialize the counter for brackets
    nested_found = False  # Flag to track if nesting is found

    for char in string:
        if char == '[':
            counter += 1  # Increment for opening bracket
            if counter > 1:  # Check for nesting
                nested_found = True
        elif char == ']':
            counter -= 1  # Decrement for closing bracket
            
            # If counter goes negative, it means there are unmatched closing brackets
            if counter < 0:
                return False

    # After processing, check if the brackets are balanced and if nesting was found
    return counter == 0 and nested_found

# Example usage
print(is_nested('[[]]'))          # True
print(is_nested('[]]]]]]][[[[[]')) # False
print(is_nested('[][]'))          # False
print(is_nested('[]'))            # False
print(is_nested('[[][]]'))        # True
print(is_nested('[[]][['))        # True
