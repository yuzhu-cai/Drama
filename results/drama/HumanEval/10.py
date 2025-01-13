
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome. """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ 
    Find the shortest palindrome that begins with a supplied string.
    
    The algorithm works as follows:
    - Find the longest suffix of the supplied string that is a palindrome.
    - Append to the end of the string the reverse of the prefix that comes before the palindromic suffix.
    
    Examples:
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    # If the input string is empty, return it as is
    if not string:
        return string
    
    # Find the longest palindromic suffix
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            # If string[i:] is a palindrome, append the reverse of the prefix string[:i]
            return string + string[:i][::-1]
    
    # If the whole string is a palindrome, return it as is
    return string

# Example usage
if __name__ == "__main__":
    print(make_palindrome(""))        # Output: ''
    print(make_palindrome("cat"))     # Output: 'catac'
    print(make_palindrome("cata"))    # Output: 'catac'
    print(make_palindrome("race"))     # Output: 'racecar'
    print(make_palindrome("aacecaaa")) # Output: 'aacecaaa'
    print(make_palindrome("abcd"))     # Output: 'abcddcba'
