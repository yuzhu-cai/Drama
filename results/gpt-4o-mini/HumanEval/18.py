
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlapping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    count = 0
    start = 0
    
    while True:
        start = string.find(substring, start)
        if start == -1:  # No more occurrences found
            break
        count += 1
        start += 1  # Move to the next character to allow for overlapping matches
    
    return count


print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
print(how_many_times('', 'a'))  # Output: 0
