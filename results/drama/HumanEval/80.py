
def is_happy(s):
    """Check if the string s is happy.
    
    A string is happy if:
    - Its length is at least 3.
    - Every 3 consecutive letters are distinct.
    
    Args:
    s (str): The input string.
    
    Returns:
    bool: True if the string is happy, False otherwise.
    """
    
    # Check if the length of the string is at least 3
    if len(s) < 3:
        return False
    
    seen_triplets = set()
    
    # Iterate through the string, stopping 2 characters before the end
    for i in range(len(s) - 2):
        triplet = s[i:i + 3]  # Get the substring of length 3
        # Check if the triplet has distinct characters
        if len(set(triplet)) != 3:
            return False  # Found a triplet with duplicate characters
        if triplet in seen_triplets:
            return False  # Found a duplicate triplet
        seen_triplets.add(triplet)  # Add the triplet to the set
    
    return True  # All conditions for being happy are satisfied

# Example usage:
print(is_happy("a"))        # Output: False
print(is_happy("aa"))       # Output: False
print(is_happy("abcd"))     # Output: True
print(is_happy("aabb"))     # Output: False
print(is_happy("adb"))      # Output: True
print(is_happy("xyy"))      # Output: False
