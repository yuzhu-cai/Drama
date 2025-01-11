
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # Find the longest palindromic suffix
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            # The suffix starting from index i is a palindrome
            suffix_length = len(string) - i
            break
    else:
        # If no palindromic suffix is found, the whole string is non-palindromic
        suffix_length = 0

    # The prefix that needs to be reversed and appended
    prefix = string[:len(string) - suffix_length]
    return string + prefix[::-1]

# Example usage
print(make_palindrome(''))       # Output: ''
print(make_palindrome('cat'))    # Output: 'catac'
print(make_palindrome('cata'))   # Output: 'catac'
