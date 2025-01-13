
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same unique characters.

    Parameters:
    s0 (str): The first string to compare.
    s1 (str): The second string to compare.

    Returns:
    bool: True if both strings have the same unique characters, False otherwise.

    Examples:
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    # Convert both strings to sets to get unique characters
    unique_chars_s0 = set(s0)
    unique_chars_s1 = set(s1)
    
    # Compare the two sets
    return unique_chars_s0 == unique_chars_s1

# Example usage
if __name__ == "__main__":
    print(same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc'))  # True
    print(same_chars('abcd', 'dddddddabc'))                # True
    print(same_chars('dddddddabc', 'abcd'))                # True
    print(same_chars('eabcd', 'dddddddabc'))               # False
    print(same_chars('abcd', 'dddddddabce'))               # False
    print(same_chars('eabcdzzzz', 'dddzzzzzzzddddabc'))   # False
