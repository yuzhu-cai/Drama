
def how_many_times(string: str, substring: str) -> int:
    """Find how many times a given substring can be found in the original string. Count overlapping cases.
    
    Args:
        string (str): The main string to search within.
        substring (str): The substring to count occurrences of.
    
    Returns:
        int: The total count of occurrences of the substring in the string, including overlaps.
    
    Examples:
        >>> how_many_times('', 'a')
        0
        >>> how_many_times('aaa', 'a')
        3
        >>> how_many_times('aaaa', 'aa')
        3
    """
    
    # Edge case: If the substring is empty, return 0
    if substring == "":
        return 0
    
    count = 0
    start = 0
    
    # Loop to find all occurrences of the substring
    while True:
        start = string.find(substring, start)
        
        # If no more occurrences are found, break the loop
        if start == -1:
            break
        
        count += 1  # Increment the count for each found occurrence
        start += 1  # Move to the next position to allow for overlapping matches
    
    return count

# Example usage
if __name__ == "__main__":
    print(how_many_times('', 'a'))        # Output: 0
    print(how_many_times('aaa', 'a'))     # Output: 3
    print(how_many_times('aaaa', 'aa'))   # Output: 3
    print(how_many_times('ababcabc', 'abc'))  # Output: 2
