
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) it consists of.
    
    Args:
        string (str): The input string to analyze.
        
    Returns:
        int: The count of distinct characters in the string, ignoring case.
    
    Examples:
        >>> count_distinct_characters('xyzXYZ')
        3
        >>> count_distinct_characters('Jerry')
        4
    """
    # Convert the string to lowercase to ensure case insensitivity
    lower_string = string.lower()
    
    # Create a set from the characters of the lowercase string to filter out duplicates
    unique_characters = set(lower_string)
    
    # Return the length of the set, which represents the count of distinct characters
    return len(unique_characters)

# Example usage
if __name__ == "__main__":
    print(count_distinct_characters('xyzXYZ'))  # Output: 3
    print(count_distinct_characters('Jerry'))    # Output: 4
