
def is_nested(string):
    # Initialize a stack to keep track of opening brackets
    stack = []
    # Variable to track if we have found a nested structure
    has_nested = False
    
    for char in string:
        if char == '[':
            # Push opening brackets onto the stack
            stack.append(char)
        elif char == ']':
            # If we encounter a closing bracket, we need to check the stack
            if stack:
                # Pop the last opening bracket from the stack
                stack.pop()
                # If we have more than one opening bracket in the stack,
                # it indicates a nested structure
                if len(stack) > 0:
                    has_nested = True
            else:
                # If there's no matching opening bracket, it's invalid
                return False
    
    # After processing all characters, we should have no unmatched opening brackets
    # and we should have found at least one nested structure
    return has_nested and len(stack) == 0

# Test cases
print(is_nested('[[]]'))  # True
print(is_nested('[]]]]]]][[[[[]'))  # False
print(is_nested('[][]'))  # False
print(is_nested('[]'))  # False
print(is_nested('[[][]]'))  # True
print(is_nested('[[]][['))  # True
