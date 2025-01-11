
def is_happy(s):
    """Check if the string is happy."""
    # Check if the length of the string is at least 3
    if len(s) < 3:
        return False
    
    # Iterate through the string, checking every 3 consecutive characters
    for i in range(len(s) - 2):
        # Get the current group of 3 characters
        group = s[i:i+3]
        # Check if all characters in the group are distinct
        if len(set(group)) < 3:  # If the length of the set is less than 3, there are duplicates
            return False
    
    # If all groups of 3 characters are distinct, return True
    return True

# Test cases
print(is_happy("a"))      # False
print(is_happy("aa"))     # False
print(is_happy("abcd"))   # True
print(is_happy("aabb"))   # False
print(is_happy("adb"))    # True
print(is_happy("xyy"))    # False
